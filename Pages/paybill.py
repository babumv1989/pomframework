from Pages.basepage import BasePage
from selenium.webdriver.common.by import By


class PayBill(BasePage):
    add_new_payee = By.XPATH, "//a[text()='Add New Payee']"
    payeename = By.ID, "np_new_payee_name"
    payeeadress = By.ID, "np_new_payee_address"
    payeeaccount = By.ID, "np_new_payee_account"
    payeedetails = By.ID, "np_new_payee_details"
    add_payee_link = By.ID, "add_new_payee"

    def click_add_new_payee(self):
        self._click(self.add_new_payee)

    def do_enter_payee_details(self, P_name, P_address, P_account, P_details):
        self.wait_for_element(self.payeename, "visibility").send_keys(P_name)
        self.enter_text(self.payeeadress, P_address)
        self.enter_text(self.payeeaccount, P_account)
        self.enter_text(self.payeedetails, P_details)
        self._click(self.add_payee_link)




