from locators.order_taxi_page_locators import OrderTaxiPageLocators
from pages.base_page import BasePage

class OrderTaxiPage(BasePage):

    def _build_locator(self, template, **kwargs):
        by, xpath = template
        return by, xpath.format(**kwargs)

    def is_order_form_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.ORDER_FORM)

    def count_visible_tariffs(self):
        return sum(
            1 for loc in OrderTaxiPageLocators.ALL_TARIFF_LOCATORS
            if self.is_visible(loc)
        )

    def is_any_tariff_active(self):
        return self.is_present(OrderTaxiPageLocators.TARIFF_ACTIVE)

    def click_tariff_work(self):
        self.click(OrderTaxiPageLocators.TARIFF_WORK)

    def click_tariff_by_name(self, tariff_name):
        self.click(self._build_locator(OrderTaxiPageLocators.TARIFF_TITLE_TEMPLATE, tariff_name=tariff_name))  

    def hover_tariff_info_icon(self, tariff_name):
        self.hover(self._build_locator(OrderTaxiPageLocators.TARIFF_INFO_ICON_TEMPLATE, tariff_name=tariff_name))

    def is_tooltip_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.TARIFF_TOOLTIP)

    def get_tooltip_text(self):
        return self.get_text(OrderTaxiPageLocators.TARIFF_TOOLTIP_TEXT)

    def is_phone_field_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.PHONE_FIELD)

    def is_payment_field_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.PAYMENT_FIELD)

    def is_comment_field_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.COMMENT_FIELD)

    def is_requirements_block_displayed(self):
        return self.is_visible(OrderTaxiPageLocators.REQUIREMENTS_BLOCK)

    def enable_laptop_table_switch(self):
        self.click(OrderTaxiPageLocators.LAPTOP_TABLE_SWITCH)

    def click_enter_number_button(self):
        self.click(OrderTaxiPageLocators.ENTER_NUMBER_BUTTON)

    def get_tariff_price(self, tariff_name):
        return self.get_text(self._build_locator(OrderTaxiPageLocators.TARIFF_PRICE_TEMPLATE, tariff_name=tariff_name))

    def wait_for_order_form(self):
        self.find_visible(OrderTaxiPageLocators.ORDER_FORM)
