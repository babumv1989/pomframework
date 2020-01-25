from Pages.basepage import BasePage
from selenium.webdriver.common.by import By


class AccountSummary(BasePage):
    paybills_link = By.XPATH, "//a[text()='Pay Bills']"

    def click_pay_bills(self):
        self._click(self.paybills_link)
