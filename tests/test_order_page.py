import allure
import pytest

from data import Scooter
from helper import Helper
from locators.dzen_locator import DzenLocators
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Тест страницы заказа')
    @allure.step('Тестируем переход на страницу заказа через верхнюю кнопку "Заказать"')
    def test_upper_order_button(self, driver):
        upper_order_button = OrderPage(driver)
        upper_order_button.click_cookie_button()
        upper_order_button.wait_and_find_element(OrderPageLocators.UPPER_ORDER_BUTTON).click()
        assert driver.current_url == Scooter.URL_ORDER

    @allure.step('Тестируем переход на страницу заказа через нижнюю кнопку "Заказать"')
    def test_lower_order_button(self, driver):
        lower_order_button = OrderPage(driver)
        lower_order_button.click_cookie_button()
        lower_order_button.wait_and_find_element(OrderPageLocators.LOWER_ORDER_BUTTON).click()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

    @allure.step('Тестируем заполнение формы заказа')
    @allure.description('Заполняем валидными данными форму заказ, тестируем с двумя разными наборами данных')
    @pytest.mark.parametrize(Scooter.FORM_PARAMETERS, Helper.parametrize_massive_order())
    def test_order_form(self, driver, name, surname, address, metro_station, telephone, comment):
        order_page = OrderPage(driver)
        order_page.click_cookie_button()
        order_page.click_element(OrderPageLocators.UPPER_ORDER_BUTTON)
        order_page.filling_text_field(OrderPageLocators.NAME_FIELD, name)
        order_page.filling_text_field(OrderPageLocators.SURNAME_FIELD, surname)
        order_page.filling_text_field(OrderPageLocators.ADDRESS_FIELD, address)
        order_page.click_element(OrderPageLocators.METRO_STATION_DROPDOWN_LIST)
        order_page.click_element(OrderPageLocators.element_by_xpath_text(metro_station))
        order_page.filling_text_field(OrderPageLocators.TELEPHONE_FIELD, telephone)
        order_page.click_element(OrderPageLocators.NEXT_BUTTON)
        order_page.click_element(OrderPageLocators.CALENDAR)
        order_page.click_element(OrderPageLocators.PRESENT_DATE)
        order_page.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        order_page.click_element(OrderPageLocators.RENTAL_PERIOD)
        order_page.click_element(OrderPageLocators.SCOOTER_COLOR)
        order_page.filling_text_field(OrderPageLocators.COMMENT_FIELD, comment)
        order_page.click_element(OrderPageLocators.FINISH_ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        assert 'Заказ оформлен' in order_page.wait_and_find_element(OrderPageLocators.CONFIRM_ORDER_TEXT).text

    @allure.step('Тестируем клик на логотип "Самокат"')
    def test_scooter_logo(self, driver):
        scooter_logo = OrderPage(driver)
        scooter_logo.click_cookie_button()
        scooter_logo.click_element(OrderPageLocators.LOWER_ORDER_BUTTON)
        scooter_logo.click_element(OrderPageLocators.SCOOTER_LOGO)
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Тестируем клик на логотип "Yandex"')
    def test_yandex_logo(self, driver):
        yandex_logo = OrderPage(driver)
        yandex_logo.click_cookie_button()
        yandex_logo.click_element(OrderPageLocators.LOWER_ORDER_BUTTON)
        yandex_logo.click_element(OrderPageLocators.YANDEX_LOGO)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        yandex_logo.wait_and_find_element(DzenLocators.FIND_BUTTON)
        assert Scooter.URL_DZEN in driver.current_url and len(windows) == 2
