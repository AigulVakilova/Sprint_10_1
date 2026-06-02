from locators.search_page_locators import SearchPageLocators
from pages.base_page import BasePage

class SearchPage(BasePage):

    def is_search_window_displayed(self):
        return self.is_visible(SearchPageLocators.SEARCH_WINDOW)

    def get_search_title_text(self):
        return self.get_text(SearchPageLocators.SEARCH_TITLE)

    def is_timer_displayed(self):
        return self.is_visible(SearchPageLocators.COUNTDOWN_TIMER)

    def is_cancel_button_displayed(self):
        return self.is_visible(SearchPageLocators.CANCEL_BUTTON)

    def is_details_button_displayed(self):
        return self.is_visible(SearchPageLocators.DETAILS_BUTTON)

    def click_details_button(self):
        self.click(SearchPageLocators.DETAILS_BUTTON)

    def click_cancel_button(self):
        self.click(SearchPageLocators.CANCEL_BUTTON)

    def is_details_block_displayed(self):
        return self.is_visible(SearchPageLocators.DETAILS_BLOCK)

    def get_details_address_from(self):
        return self.get_text(SearchPageLocators.DETAILS_ADDRESS_FROM)

    def get_details_address_to(self):
        return self.get_text(SearchPageLocators.DETAILS_ADDRESS_TO)

    def get_details_payment(self):
        return self.get_text(SearchPageLocators.DETAILS_PAYMENT)

    def is_details_trip_info_displayed(self):
        return self.is_visible(SearchPageLocators.DETAILS_TRIP_INFO)

    def get_details_cost(self):
        return self.get_text(SearchPageLocators.DETAILS_COST)

    def wait_for_completed_order(self, timeout=90):
        self.wait_for_element_visible(SearchPageLocators.ORDER_NUMBER, timeout=timeout)

    def is_completed_order_displayed(self):
        return self.is_visible(SearchPageLocators.COMPLETED_TITLE)

    def get_completed_title_text(self):
        return self.get_text(SearchPageLocators.COMPLETED_TITLE)

    def is_car_number_displayed(self):
        return self.is_visible(SearchPageLocators.CAR_NUMBER)

    def is_car_image_displayed(self):
        return self.is_visible(SearchPageLocators.CAR_IMAGE)

    def is_driver_rating_displayed(self):
        return self.is_visible(SearchPageLocators.DRIVER_RATING)

    def is_driver_name_displayed(self):
        return self.is_visible(SearchPageLocators.DRIVER_NAME)

    def is_driver_photo_displayed(self):
        return self.is_visible(SearchPageLocators.DRIVER_PHOTO)

    def is_search_window_closed(self):
        try:
            self.wait_for_element_invisible(SearchPageLocators.SEARCH_WINDOW, timeout=5)
            return True
        except Exception:
            return False
        