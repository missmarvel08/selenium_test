import os
import requests
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ArticlePage(BasePage):
    ARTICLE_CONTENT = (By.CSS_SELECTOR, "div.article-content")  # Change selector if needed
    IMAGE = (By.CSS_SELECTOR, "img.cover-image")  # Cover image selector

    def get_article_content(self):
        return self.get_text(self.ARTICLE_CONTENT)

    def get_article_image(self):
        image_element = self.find_element(self.IMAGE)
        return image_element.get_attribute("src")

    def download_image(self, image_url, filename):
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(os.path.join("images", filename), "wb") as f:
                f.write(response.content)