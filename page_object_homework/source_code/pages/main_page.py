from page_object_homework.source_code.pages.common_page import CommonPage
from page_object_homework.source_code.constants import Host


class MainPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self):
        self.open(Host.MY_FIN)
