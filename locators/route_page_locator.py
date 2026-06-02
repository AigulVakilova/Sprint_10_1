from selenium.webdriver.common.by import By

class RoutePageLocators:
    ROUTE_TAB_OPTIMAL = (By.XPATH, "//div[@class='modes-container']//div[contains(@class,'mode') and text()='Оптимальный']")
    ROUTE_TAB_FAST = (By.XPATH, "//div[@class='modes-container']//div[contains(@class,'mode') and text()='Быстрый']")
    ROUTE_TAB_CUSTOM = (By.XPATH, "//div[@class='modes-container']//div[contains(@class,'mode') and text()='Свой']")
    ROUTE_TAB_ACTIVE = (By.XPATH, "//div[@class='modes-container']//div[@class='mode active']")
    ROUTE_BLOCK = (By.CLASS_NAME, "results-container")
    ROUTE_PRICE = (By.XPATH, "//div[@class='results-text']//div[@class='text']")
    ROUTE_TIME = (By.XPATH, "//div[@class='results-text']//div[@class='duration']")
    TRANSPORT_ALL = (By.XPATH, "//div[@class='types-container']/div")
    TRANSPORT_DRIVE = (By.XPATH, "//div[@class='types-container']//div[@class='type drive']")
    CALL_TAXI_BUTTON = (By.XPATH, "//div[@class='results-text']//button[@class='button round' and text()='Вызвать такси']")
    BOOK_DRIVE_BUTTON = (By.XPATH, "//div[@class='results-text']//button[@class='button round' and text()='Забронировать']")
