import pytest
from selenium import webdriver
from datetime import datetime, timedelta
from locators.main_page_locators import MainPage
from locators.order_page_locators import OrderPage

url = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()