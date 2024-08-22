from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators


class OrderPageLocators(MainPageLocators):
    # Локаторы формы заказа
    NAME_FIELD = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
    SURNAME_FIELD = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
    ADDRESS_FIELD = (By.XPATH, '//input[contains(@placeholder, "Адрес")]')
    METRO_STATION_DROPDOWN_LIST = (By.XPATH, f'//input[contains(@placeholder, "Станция метро")]')
    TELEPHONE_FIELD = (By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    NEXT_BUTTON = (By.XPATH, '//button[text() = "Далее"]')
    CALENDAR = (By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]')
    PRESENT_DATE = (By.XPATH, '//*[contains(@class, "selected")]')
    RENTAL_PERIOD_FIELD = (By.XPATH, '// *[contains(text(), "Срок аренды")]')
    RENTAL_PERIOD = (By.XPATH, '//*[text()="сутки"]')
    SCOOTER_COLOR = (By.XPATH, '//*[text()="чёрный жемчуг"]')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')
    FINISH_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"Button_Middle__1CSJM") and text()="Заказать"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    CONFIRM_ORDER_TEXT = (By.XPATH, '//*[text()="Заказ оформлен"]')
    ORDER_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    SCOOTER_LOGO = (By.XPATH, '//*[contains(@class,"LogoScooter")]')
    YANDEX_LOGO = (By.XPATH, '//*[contains(@class,"LogoYandex")]')
