from selenium.webdriver.common.by import By


class TestClass:
    def test_selenium_second(self, driver):
        driver.get('https://www.thesaurus.com/')
        our_first_element = driver.find_element(By.XPATH, "//*[@id='global-search']")
        our_first_element.send_keys('love')
        find_button = driver.find_element(By.XPATH, "//*[@type='submit' and @data-type='button']")
        find_button.click()
        sixth_synonym = driver.find_element(By.XPATH, "//*[contains(@href, '/friendship')]")
        print(f'The sixth synonym is {sixth_synonym.text}')
        first_synonyms = driver.find_elements(By.XPATH, "//*[contains(@class, 'ESLI_')]")
        second_synonyms = driver.find_elements(By.XPATH, "//*[contains(@class, ' DL3p3OH7u8i4dIoN1ag')]")
        third_synonyms = driver.find_elements(By.XPATH, "//*[contains(@class, '_JJhtba_')]")
        all_synonyms = first_synonyms + second_synonyms + third_synonyms
        for word in all_synonyms:
            print(f'Another synonym is {word.text}')


