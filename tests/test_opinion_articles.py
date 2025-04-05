import re
import sys
import os
import threading
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from pages.home_page import HomePage
from pages.opinion_page import OpinionPage
from pages.article_page import ArticlePage
from utils.translate import translate_text
from utils.browserstack_config import get_browserstack_driver

os.makedirs("images", exist_ok=True)

class TestOpinionArticles:
    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver)
        self.opinion_page = OpinionPage(driver)
        self.article_page = ArticlePage(driver)

    def run_test(self):
        self.home_page.open_url("https://elpais.com/")
        self.home_page.navigate_to_opinion()
        articles = self.opinion_page.get_article_links()

        translated_titles = []
        for title, link in articles:
            self.driver.get(link)
            content = self.article_page.get_article_content()
            image_url = self.article_page.get_article_image()

            print(f"Title: {title}\nContent: {content[:500]}...\n")
            if image_url:
                filename = title.replace(" ", "_") + ".jpg"
                self.article_page.download_image(image_url, filename)

            translated_title = translate_text(title)
            print(f"Translated Title: {translated_title}\n")
            translated_titles.append(translated_title)

        # Analyze repeated words
        self.analyze_headers(translated_titles)

    def analyze_headers(self, translated_titles):
        words = re.findall(r'\b\w+\b', " ".join(translated_titles).lower())
        word_counts = {word: words.count(word) for word in set(words) if words.count(word) > 2}

        print("\nRepeated Words:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

# Run tests on BrowserStack in parallel
def run_on_browserstack(browser, os_name):
    driver = get_browserstack_driver(browser, os_name)
    test = TestOpinionArticles(driver)
    test.run_test()
    driver.quit()

browsers = [
    ("Chrome", "Windows"),
    ("Firefox", "Windows"),
    ("Edge", "Windows"),
    ("Safari", "Mac"),
    ("Chrome", "Android")
]

threads = []
for browser, os_name in browsers:
    t = threading.Thread(target=run_on_browserstack, args=(browser, os_name))
    t.start()
    threads.append(t)

for t in threads:
    t.join()