from playwright.sync_api import Page, expect
from utilities.randomData import RandomData
from utilities.ConfigReader import ConfigFileReader


class InfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_textField = page.get_by_placeholder("First Name")
        self.last_name_textField = page.get_by_placeholder("Last Name")
        self.postal_code_textField = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def enter_checkout_information(self):
        try:
            randomData = RandomData()
            first_name = randomData.get_first_name()
            last_name = randomData.get_last_name()
            postal_code = randomData.get_zipcode()
            self.first_name_textField.fill(first_name)
            self.last_name_textField.fill(last_name)
            self.postal_code_textField.fill(postal_code)
            self.continue_button.click()
            config_reader = ConfigFileReader()
            overview_URL = config_reader.readConfig("basic info", "overviewURL")
            expect(self.page).to_have_url(overview_URL)
        except:
            print("Error occured while entering checkout information")