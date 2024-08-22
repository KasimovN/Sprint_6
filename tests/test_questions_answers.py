import allure
import pytest
from helper import Helper
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestQuestionsAnswers:
    @allure.title('Проверка вопроса/ответа')
    @allure.description('Проверка на тексты вопросов/ответов и на сопоставления ответов нужным вопросам')
    @pytest.mark.parametrize('question, answer', Helper.parametrize_massive_qa())
    def test_question(self, driver, question, answer):
        main_page = MainPage(driver)
        q_locator = MainPageLocators.element_by_xpath_text(question)
        q_element = main_page.wait_and_find_element(q_locator)
        main_page.click_cookie_button()
        main_page.scroll_page_to_footer(driver)
        main_page.click_element(q_locator)
        a_locator = MainPageLocators.element_by_xpath_text(answer)
        a_element = main_page.wait_and_find_element(a_locator)
        assert q_element.text == question and a_element.text == answer
