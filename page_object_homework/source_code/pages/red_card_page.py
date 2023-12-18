from page_object_homework.source_code.pages.common_page import CommonPage


class RedCardPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.input_area = "//*[contains(@class, 'input') and @type='tel']"

        self.confirmation_button = "//*[contains(@class, 'button') and @type='submit']"

        self.msi_button = "//*[@class='actionButtons']//*[@type='button']"

    def background_color(self):
        color = self.color_of_a_button(self.msi_button, "background-color")
        return color

    def rgba_to_hex(self, rgba_color, hex_color):
        rgba_numbers = rgba_color[5:-1]
        rgba_lst = list(map(int, rgba_numbers.split(',')))
        r, g, b, a = rgba_lst
        color = f"#{r:02x}{g:02x}{b:02x}"
        assert color == hex_color
