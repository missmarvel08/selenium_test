from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    OPINION_SECTION = (By.LINK_TEXT, "Opinión")

    def navigate_to_opinion(self):
        self.click(self.OPINION_SECTION)