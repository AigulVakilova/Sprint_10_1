from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def set_address_from(self, address):
        self.click(MainPageLocators.FROM_LABEL)
        self.type_text(MainPageLocators.FROM_INPUT, address)

    def set_address_to(self, address):
        self.click(MainPageLocators.TO_LABEL)
        self.type_text(MainPageLocators.TO_INPUT, address)

    def is_from_pin_displayed(self):
        return self.is_visible(MainPageLocators.MAP_FROM_PIN)

    def is_to_pin_displayed(self):
        return self.is_visible(MainPageLocators.MAP_TO_PIN)

    def is_route_block_displayed(self):
        return self.is_visible(MainPageLocators.ROUTE_BLOCK)
