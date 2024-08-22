from selenium.webdriver.common.by import By


class MainPageLocators:

    UPPER_ORDER_BUTTON = (By.XPATH, '//*[@class ="Button_Button__ra12g" and text() ="Заказать"]')
    LOWER_ORDER_BUTTON = (By.XPATH, '//div[@class ="Home_FinishButton__1_cWm"]/button')
    COOKIE_BUTTON = (By.XPATH, '//*[text()="да все привыкли"]')

    @staticmethod
    def element_by_xpath_text(var):
        return By.XPATH, f'//*[text() = "{var}"]'
