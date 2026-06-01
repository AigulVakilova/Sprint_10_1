from locators.route_page_locator import RoutePageLocators
from pages.base_page import BasePage

class RoutePage(BasePage):

    def click_route_optimal(self):
        self.click(RoutePageLocators.ROUTE_TAB_OPTIMAL)

    def click_route_fast(self):
        self.click(RoutePageLocators.ROUTE_TAB_FAST)

    def click_route_custom(self):
        self.click(RoutePageLocators.ROUTE_TAB_CUSTOM)

    def is_route_block_displayed(self):
        return self.is_visible(RoutePageLocators.ROUTE_BLOCK)

    def get_route_block_text(self):
        return self.get_text(RoutePageLocators.ROUTE_BLOCK)

    def get_active_tab_text(self):
        return self.get_text(RoutePageLocators.ROUTE_TAB_ACTIVE)

    def is_optimal_tab_active(self):
        return self.get_active_tab_text() == "Оптимальный"

    def is_fast_tab_active(self):
        return self.get_active_tab_text() == "Быстрый"

    def is_custom_tab_active(self):
        return self.get_active_tab_text() == "Свой"

    def get_route_price(self):
        return self.get_text(RoutePageLocators.ROUTE_PRICE)

    def get_route_time(self):
        return self.get_text(RoutePageLocators.ROUTE_TIME)

    def are_all_transport_types_displayed(self):
        elements = self.find_all(RoutePageLocators.TRANSPORT_ALL)
        return len(elements) == 6

    def click_transport_drive(self):
        self.click(RoutePageLocators.TRANSPORT_DRIVE)

    def is_call_taxi_button_displayed(self):
        return self.is_visible(RoutePageLocators.CALL_TAXI_BUTTON)

    def is_call_taxi_button_enabled(self):
        return self.is_element_enabled(RoutePageLocators.CALL_TAXI_BUTTON)

    def is_book_drive_button_displayed(self):
        return self.is_visible(RoutePageLocators.BOOK_DRIVE_BUTTON)

    def is_book_drive_button_enabled(self):
        return self.is_element_enabled(RoutePageLocators.BOOK_DRIVE_BUTTON)

    def click_call_taxi(self):
        self.click(RoutePageLocators.CALL_TAXI_BUTTON)

    def click_book_drive(self):
        self.click(RoutePageLocators.BOOK_DRIVE_BUTTON)
