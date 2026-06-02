from selenium.webdriver.common.by import By

class OrderTaxiPageLocators:
    ORDER_FORM = (By.CLASS_NAME, "tariff-picker")
    TARIFF_ACTIVE = (By.XPATH, "//div[@class='tcard active']")
    TARIFF_WORK = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Рабочий']]")
    TARIFF_SLEEPY = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Сонный']]")
    TARIFF_VACATION = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Отпускной']]")
    TARIFF_TALKATIVE = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Разговорчивый']]")
    TARIFF_COMFORT = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Утешительный']]")
    TARIFF_GLOSSY = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='Глянцевый']]")
    TARIFF_TOOLTIP = (By.XPATH, "//div[contains(@class,'i-floating-tooltip')]//div[@class='i-floating']")
    TARIFF_TOOLTIP_TEXT = (By.XPATH, "//div[contains(@class,'i-floating-tooltip')]//div[@class='i-dPrefix']")
    TARIFF_TITLE_TEMPLATE = (By.XPATH, "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='{tariff_name}']]")
    PHONE_FIELD = (By.CLASS_NAME, "np-button")
    PAYMENT_FIELD = (By.CLASS_NAME, "pp-button")
    COMMENT_FIELD = (By.ID, "comment")
    REQUIREMENTS_BLOCK = (By.CLASS_NAME, "reqs")
    LAPTOP_TABLE_SWITCH = (By.XPATH, "//div[@class='r-sw-label' and text()='Столик для ноутбука']/following-sibling::div[@class='r-sw']")
    ENTER_NUMBER_BUTTON = (By.CLASS_NAME, "smart-button")

    ALL_TARIFF_LOCATORS = [
        TARIFF_WORK,
        TARIFF_SLEEPY,
        TARIFF_VACATION,
        TARIFF_TALKATIVE,
        TARIFF_COMFORT,
        TARIFF_GLOSSY,
    ]

    TARIFF_INFO_ICON_TEMPLATE = (
        By.XPATH,
        "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='{tariff_name}']]//button[contains(@class,'i-button')]"
    )
    TARIFF_PRICE_TEMPLATE = (
        By.XPATH,
        "//div[contains(@class,'tcard') and .//div[@class='tcard-title' and text()='{tariff_name}']]//div[@class='tcard-price']"
    )
