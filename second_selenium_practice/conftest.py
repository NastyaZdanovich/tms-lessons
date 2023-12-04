import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options) as driver:
        yield driver
