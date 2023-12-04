import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


class TestSelenium:
    @pytest.mark.parametrize('url, page_title', [
        ('https://www.amazon.com/', 'Amazon'),
        ('https://www.apple.com/', 'Apple'),
        ('https://www.google.com/', 'Google')])
    def test_selenium(self, driver, url, page_title):
        driver.get(url)
        page_title = driver.title
        if 'Google' not in page_title:
            driver.save_screenshot(f'{page_title}.png')
            raise Exception('Something is wrong')