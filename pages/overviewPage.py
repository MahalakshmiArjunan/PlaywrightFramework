from playwright.sync_api import Page,expect
from utilities.ConfigReader import ConfigFileReader


class OverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.get_by_role("button", name="Finish")
        self.back_home_button = page.get_by_role("button", name="Back Home")

    def placeOrder(self):
        try:
            self.finish_button.click()
            config_reader = ConfigFileReader()
            finish_URL = config_reader.readConfig("basic info", "finishURL")
            expect(self.page).to_have_url(finish_URL)
            self.back_home_button.click()
            dashboard_URL = config_reader.readConfig("basic info", "dashboardURL")
            expect(self.page).to_have_url(dashboard_URL)
        except:
            print("Error occured while proceeding to dashboard")
            
