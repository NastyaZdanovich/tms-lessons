import re


def check_a_phone_number(phone_numbers):
    phone_numbers = phone_numbers[4:]
    phone_number_type = r'^8 \(\d{3}\) \d{3}-\d{2}-\d{2}$'
    if re.match(phone_number_type, phone_numbers):
        print(f'{phone_numbers} is a valid phone number.')
    else:
        print('Something is wrong.')


class TestClass:
    def test_new(self, page):
        page.goto("https://blizko.by/")
        catalog_button = page.get_by_role("link", name="Каталог")
        catalog_button.click()
        page.wait_for_url("**/companies")
        house_button = page.get_by_text("Дом", exact=True)
        house_button.click()
        house_items = page.get_by_role("link", name="Товары для дома")
        house_items.click()
        phone_numbers_button = page.get_by_role("link", name="Телефоны").first
        phone_numbers_button.click()
        title_name = page.locator("#modalSet").get_by_text("Салон штор «Виджи дизайн»")
        phone_number = page.get_by_role("link", name="(017) 270-60-12")

        get_a_phone_number = phone_number.get_attribute("href")
        check_a_phone_number(get_a_phone_number)

        current_weight = int(title_name.evaluate(
            "(e) => {return"
            " window.getComputedStyle(e).getPropertyValue('font-weight');"
            "}"))
        assert current_weight >= 700

# Я не поняла, как проверить, что что-то является просто текстом. Объясните, пожалуйста, на лекции.