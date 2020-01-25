from Pages.basepage import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    __signin_button = By.XPATH, "//button[@id='signin_button']"

    def click_signin_button(self):
        self._click(self.__signin_button)


