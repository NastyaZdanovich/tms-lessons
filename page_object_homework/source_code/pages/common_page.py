from page_object_homework.source_code.constants import Host
from page_object_homework.source_code.pages.base_page import BasePage


class CommonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.cards_button = "//*[contains(@href, 'cards') and contains(@onclick, 'Karty')]"

        self.red_card_button = "//*[@title='Красная карта 2.0']"

    def open_main_page(self):
        self.open(Host.MY_FIN)

    def hover_over_cards_button(self):
        self.hover(self.cards_button)
