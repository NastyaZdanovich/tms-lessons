from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def assert_element(self, xpath, clickable=False, return_many=False):
        driver = self.driver
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

    def open(self, url):
        self.driver.get(url)

    def click(self, xpath):
        element = self.assert_element(xpath, clickable=True)

        element.click()

    def hover(self, xpath):
        actions = ActionChains(self.driver)
        element = self.assert_element(xpath)
        actions.move_to_element(element).perform()

    def assert_current_url(self, target_url):
        current_url = self.driver.current_url

        assert target_url in current_url, f'f{target_url} is not in {current_url}'

    def fill_in_a_form(self, xpath, value):
        element = self.assert_element(xpath)
        element.send_keys(value)

    def color_of_a_button(self, xpath, condition):
        element = self.assert_element(xpath)
        return element.value_of_css_property(condition)
