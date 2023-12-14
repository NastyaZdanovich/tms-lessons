import allure

from page_object_homework.source_code.pages.common_page import CommonPage
from page_object_homework.source_code.pages.main_page import MainPage
from page_object_homework.source_code.pages.red_card_page import RedCardPage


class TestRedCardPage:
    def test_red_card(self, driver):
        with allure.step('1. Открываем главную страницу'):
            main_page = MainPage(driver)
            main_page.open_main_page()

        with allure.step("2. Наводимся на кнопку 'Карты'"):
            common_page = CommonPage(driver)
            common_page.hover_over_cards_button()

        with allure.step("3. Нажать на кнопку 'Красная карта 2.0'"):
            common_page.click(main_page.red_card_button)
            driver.switch_to.window(driver.window_handles[-1])

        with allure.step("4. Ожидаемый результат: открылась страница 'Aльфа Банк'"):
            red_card_page = RedCardPage(driver)
            red_card_page.assert_current_url('creditcard.alfa-bank')

        with allure.step("5. Ввести номер телефона в поле для заполнения"):
            red_card_page.fill_in_a_form(red_card_page.input_area, '299402265')

        with allure.step("6. Нажать на кнопку 'Подтвердить'"):
            red_card_page.click(red_card_page.confirmation_button)

        with allure.step("7. Определить цвет кпопки 'Перейти в МСИ' и сравнить ее hex-color и rgba-color"):
            red_card_page.rgba_to_hex(red_card_page.background_color(), '#ef3124')
