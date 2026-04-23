from playwright.sync_api import Page, expect
from utilities.ConfigReader import ConfigFileReader
from utilities.ExcelData import ExcelUtility


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name = "Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_container")
        self.menu_button = page.get_by_role("button", name = "Open Menu")
        self.logout_link = page.get_by_role("button", name = "Logout")
        self.about_link = page.locator("[data-test='about-sidebar-link']")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")
        self.all_products_title = page.locator("[data-test='inventory-item-name']")
        self.product_description = page.locator("[data-test='inventory-item-desc']")
        self.back_to_products_link = page.get_by_role("button", name = "Back to products")

    def add_first_product_to_cart(self):
        try:
            self.add_to_cart_button.first.click()
            self.shopping_cart_icon.click()
            config_reader = ConfigFileReader()
            cart_URL = config_reader.readConfig("basic info", "cartURL")
            expect(self.page).to_have_url(cart_URL)
        except:
            print("Error occured while adding product to cart")

    def verify_about_page(self):
        try:
            self.menu_button.click()
            self.about_link.click()
            self.page.wait_for_load_state("networkidle")
            config_reader = ConfigFileReader()
            about_page_URL = config_reader.readConfig("basic info", "aboutURL")
            expect(self.page).to_have_url(about_page_URL)
            self.page.go_back(wait_until="networkidle")
        except:
            print("Error occured while loading the page")

    def navigate_to_product_details(self):
        try:
            # product_count = self.all_products_title.count()
            # print(product_count)
            # for i in range(product_count):
            #     product = self.all_products_title.nth(i)
            #     product.click()
            #     expect(self.product_description).to_be_visible()
            #     description = self.product_description.nth(i).text_content()
            #     print(description)
            #     print("--------------------------------------")
            #     excel_data = ExcelUtility()
            #     product_desc = excel_data.getCellData("testData/userInfo.xlsx", "Sheet2", i, 1)
            #     expect(description).to_have_text(product_desc)

            for product in self.all_products_title.all():
                product.click()
                expect(self.product_description).to_be_visible()
                print(self.product_description.inner_text())
                print("------------------------------------------")
                self.back_to_products_link.click()
                config_reader = ConfigFileReader()
                dashboard_URL = config_reader.readConfig("basic info", "dashboardURL")
                expect(self.page).to_have_url(dashboard_URL)
        except:
            print("Error occured while getting navigating to product details")

    def logout_from_application(self):
        try:
            self.menu_button.click()
            self.logout_link.click()
        except:
            print("Error occured while logging out of application")

