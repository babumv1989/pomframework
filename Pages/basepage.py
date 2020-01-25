from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    driver = None

    def __init__(self, d):
        self.driver = d

    def _click(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element(self, locator, condition):
        wait = WebDriverWait(self.driver,5)
        if condition == "visibility":
            return wait.until(ec.visibility_of_element_located(locator))
        elif condition == "clickable":
            return wait.until(ec.element_to_be_clickable(locator))




