from pages.main_page import MainPage


class OrderPage(MainPage):
    def filling_text_field(self, filling_locator, filling_text):
        filled_element = self.wait_and_find_element(filling_locator)
        filled_element.send_keys(filling_text)
