import pytest
from pages.loginPage import LoginPage
from pages.infoPage import InfoPage
from pages.overviewPage import OverviewPage
from pages.cartPage import CartPage
from pages.homePage import HomePage
from utilities.ExcelData import ExcelUtility

@pytest.mark.usefixtures("page")
class TestE2EScenarios:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.info_page = InfoPage(page)
        self.overview_page = OverviewPage(page)
        self.cart_page = CartPage(page)
        self.excel_data = ExcelUtility()

    @pytest.mark.smoke
    def test_E2EScenario1(self, page):

        userName = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        self.login_page.login_to_application(userName, password)
        self.home_page.add_first_product_to_cart()
        self.cart_page.proceed_to_checkout()
        self.info_page.enter_checkout_information()
        self.overview_page.placeOrder()

    @pytest.mark.smoke
    def test_E2EScenario2(self, page):

        userName = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        self.login_page.login_to_application(userName, password)
        self.home_page.verify_about_page()
        self.home_page.logout_from_application()

    @pytest.mark.regression
    def test_E2EScenario3(self, page):

        userName = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
        password = self.excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

        self.login_page.login_to_application(userName, password)
        self.home_page.navigate_to_product_details()
        self.home_page.logout_from_application()


