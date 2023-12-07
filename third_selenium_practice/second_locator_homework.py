import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options) as driver:
        yield driver


def assert_element(driver, xpath, clickable=False, return_many=False):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    if clickable:
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    if return_many:
        result = driver.find_elements(By.XPATH, xpath)
    else:
        result = driver.find_element(By.XPATH, xpath)
    return result


def click(driver, xpath):
    element = assert_element(driver, xpath, clickable=True)
    element.click()


def rgba_to_hex(rgba_color):
    rgba_numbers = rgba_color[5:-1]
    rgba_lst = list(map(int, rgba_numbers.split(',')))
    r, g, b, a = rgba_lst
    color = f"#{r:02x}{g:02x}{b:02x}"
    return color


def test_selenium_third(driver):
    driver.get('https://myfin.by/')
    cards_xpath = "//*[@class='main-nav_link main-nav_link--straight' and @href='/cards']"
    cards = assert_element(driver, cards_xpath)
    action = ActionChains(driver)
    action.click_and_hold(cards).perform()
    red_card_xpath = "//*[@title='Красная карта 2.0']"
    red_card = assert_element(driver, red_card_xpath)
    click(driver, red_card_xpath)
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    phone_number_xpath = "//*[@class='form-control__input_n4ddv']"
    phone_number = assert_element(driver, phone_number_xpath)
    action.scroll_to_element(phone_number).send_keys_to_element(phone_number, '299402265').perform()
    confirmation_button_xpath = "//*[contains(@class, 'button') and @type='submit']"
    confirmation_button = assert_element(driver, confirmation_button_xpath)
    action.scroll_to_element(confirmation_button).perform()
    click(driver, confirmation_button_xpath)
    msi_button_xpath = "//*[@class='actionButtons']//*[@type='button']"
    msi_button = assert_element(driver, msi_button_xpath)
    action.scroll_to_element(msi_button).perform()
    color_of_msi_button = msi_button.value_of_css_property("background-color")
    hex_color = rgba_to_hex(color_of_msi_button)
    assert hex_color == '#ef3124'
