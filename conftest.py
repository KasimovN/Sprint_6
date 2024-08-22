import pytest
from selenium import webdriver

from data import Scooter


@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.get(Scooter.URL)
    firefox.maximize_window()

    yield firefox

    firefox.quit()
