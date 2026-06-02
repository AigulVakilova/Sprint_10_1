from selenium.webdriver.common.by import By

class SearchPageLocators:
    SEARCH_WINDOW = (By.CLASS_NAME, "order")
    SEARCH_TITLE = (By.CLASS_NAME, "order-header-title")
    COUNTDOWN_TIMER = (By.CLASS_NAME, "order-header-title")

    CANCEL_BUTTON = (By.XPATH, "//div[@class='order-btn-group' and .//div[text()='Отменить']]//button[@class='order-button']")
    DETAILS_BUTTON = (By.XPATH, "//div[@class='order-btn-group' and .//div[text()='Детали']]//button[@class='order-button']")

    DETAILS_BLOCK = (By.XPATH, "//div[contains(@class,'order-details')]")
    DETAILS_ADDRESS_FROM = (By.XPATH, "//div[@class='order-details-row' and .//div[@class='o-d-sh' and text()='Адрес подачи']]//div[@class='o-d-h']")
    DETAILS_ADDRESS_TO = (By.XPATH, "//div[@class='order-details-row' and .//div[@class='o-d-sh' and text()='Адрес назначения']]//div[@class='o-d-h']")
    DETAILS_PAYMENT = (By.XPATH, "//div[@class='order-details-row' and .//div[@class='o-d-sh' and text()='Способ оплаты']]//div[@class='o-d-h']")
    DETAILS_TRIP_INFO = (By.XPATH, "//div[@class='order-details-row' and .//div[@class='o-d-h' and text()='Еще про поездку']]")
    DETAILS_COST = (By.XPATH, "//div[@class='order-details-row' and .//div[@class='o-d-h' and text()='Еще про поездку']]//div[@class='o-d-sh']")

    COMPLETED_TITLE = (By.CLASS_NAME, "order-header-title")
    ORDER_NUMBER = (By.CLASS_NAME, "order-number")
    CAR_NUMBER = (By.XPATH, "//div[@class='number']")
    CAR_IMAGE = (By.XPATH, "//div[@class='order-number']//img")

    DRIVER_RATING = (By.CLASS_NAME, "order-btn-rating")
    DRIVER_NAME = (By.XPATH, "//div[@class='order-button']/following-sibling::div[not(@class)]")
    DRIVER_PHOTO = (By.XPATH, "//div[@class='order-btn-rating']//img")
    