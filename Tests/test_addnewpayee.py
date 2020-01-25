import pytest
from Pages.accountsummary import AccountSummary
from Pages.homepage import Homepage
from Pages.loginpage import Loginpage
from Pages.paybill import PayBill
from Testdata.read_excel_data import get_data


class Test_AddNewPayee:

    @pytest.fixture(scope="class", autouse=True)
    def pre_req(self, driver):
        home = Homepage(driver)
        home.click_signin_button()
        login = Loginpage(driver)
        login.do_login("username", "password")
        paybill = AccountSummary(driver)
        paybill.click_pay_bills()

    @pytest.fixture(autouse=True)
    def nav_addnewpayee(self, driver):
        self.addnewpayee = PayBill(driver)
        self.addnewpayee.click_add_new_payee()

    @pytest.mark.parametrize("name, address, account, details", get_data())
    def test_add_new_payee(self,name, address, account, details):
        self.addnewpayee.do_enter_payee_details(name, address, str(account), details)
