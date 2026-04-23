from playwright.sync_api import Page, expect
from utilities.ConfigReader import ConfigFileReader


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="checkout")

    def proceed_to_checkout(self):
        try:
            self.checkout_button.click()
            config_reader = ConfigFileReader()
            your_info_URL = config_reader.readConfig("basic info", "yourInfoURL")
            expect(self.page).to_have_url(your_info_URL)
        except:
            print("Error occured while proceeding to checkout")