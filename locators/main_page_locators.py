from selenium.webdriver.common.by import By


class MainPageLocators:

    UPPER_ORDER_BUTTON = (By.XPATH, '//div[contains(@class,"Header_Nav")]/button[ text() ="Заказать"]')
    LOWER_ORDER_BUTTON = (By.XPATH, '//div[@class ="Home_FinishButton__1_cWm"]/button')
    COOKIE_BUTTON = (By.XPATH, '//*[text()="да все привыкли"]')

    @staticmethod
    def element_by_xpath_text(var):
        return By.XPATH, f'//*[text() = "{var}"]'
