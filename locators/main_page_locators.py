from selenium.webdriver.common.by import By

class MainPageLocators:
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    FROM_LABEL = (By.XPATH, "//label[@for='from']")
    TO_LABEL = (By.XPATH, "//label[@for='to']")
    MAP_FROM_PIN = (By.XPATH, "//ymaps[contains(@class,'route-pin__text')]//*[contains(text(),'Хамовнический')]")
    MAP_TO_PIN = (By.XPATH, "//ymaps[contains(@class,'route-pin__text')]//*[contains(text(),'Зубовский')]")
    ROUTE_BLOCK = (By.CLASS_NAME, "results-container")
    