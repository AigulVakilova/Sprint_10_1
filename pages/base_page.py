from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def is_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    def hover(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        ActionChains(self.driver).move_to_element(element).perform()

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_element_enabled(self, locator):
        element = self.find(locator)
        return element.is_enabled()

    def is_element_active(self, locator):
        element = self.find(locator)
        return "active" in element.get_attribute("class")

    def get_attribute(self, locator, attr):
        return self.find(locator).get_attribute(attr)

    def wait_for_element_visible(self, locator, timeout=None):
        t = timeout or self.TIMEOUT
        return WebDriverWait(self.driver, t).until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator, timeout=None):
        t = timeout or self.TIMEOUT
        return WebDriverWait(self.driver, t).until(EC.invisibility_of_element_located(locator))
    