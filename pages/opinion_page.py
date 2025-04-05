from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpinionPage(BasePage):
    ARTICLE_TITLES = (By.CSS_SELECTOR, "h2 a")  # Selector for article titles
    ARTICLE_LINKS = (By.CSS_SELECTOR, "h2 a")  # Article links

    def get_article_links(self):
        articles = self.find_elements(self.ARTICLE_LINKS)[:5]  # First 5 articles
        return [(article.text, article.get_attribute("href")) for article in articles]