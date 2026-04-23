
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.cartPage import CartPage
from pages.infoPage import InfoPage
from pages.overviewPage import OverviewPage
from utilities.ExcelData import getCellData

def test_first_script(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)
    info_page = InfoPage(page)
    overview_page = OverviewPage(page)

    userName = getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
    password = getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)
    login_page.login_to_application(userName, password)
    home_page.add_first_product_to_cart()
    cart_page.proceed_to_checkout()
    info_page.enter_checkout_information()
    overview_page.placeOrder()
