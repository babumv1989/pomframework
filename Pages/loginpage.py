from Pages.basepage import BasePage
from selenium.webdriver.common.by import By


class Loginpage(BasePage):

    username_input = By.XPATH, "//input[@id='user_login']"
    password_input = By.XPATH, "//input[@id='user_password']"
    sigin_input = By.XPATH, "//input[@name='submit']"


    def do_login(self, uname, pword):
        self.enter_text(self.username_input, uname)
        self.enter_text(self.password_input, pword)
        self._click(self.sigin_input)
