from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPage
import random

a = random.randint(926, 960)
b = random.randint(926, 960)
c = random.randint(11, 99)
d = random.randint(11, 99)
random_phone = f'8{a}{b}{c}{d}'

class User:

    # 1-й вариант данных
    firstname_1 = 'Павел'
    secondname_1 = 'Михайлович'
    address_1 = 'Москва, Красносельская, 1'
    station_1 = 'Красносельская'
    phone_1 = random_phone
    date_1 = '15.03.2023'
    days_1 = 1
    color_1 = 'grey'
    comment_1 = 'Комментарий'

    # 2-й вариант данных
    firstname_2 = 'Игорь'
    secondname_2 = 'Петрович'
    address_2 = 'Москва, Театральная, 1'
    station_2 = 'Театральная'
    phone_2 = random_phone
    date_2 = '20.03.2023'
    days_2 = 5
    color_2 = 'black'
    comment_2 = 'Комментарий'

class Order:

    def __init__(self, driver):
        self.driver = driver

    # Заполняем первую страницу формы заказа
    def first_form(self, name, secondname, address, station, phone):
        self.driver.find_element(*OrderPage.name).send_keys(name)
        self.driver.find_element(*OrderPage.secondname).send_keys(secondname)
        self.driver.find_element(*OrderPage.address).send_keys(address)
        self.driver.find_element(*OrderPage.station).click()
        self.driver.find_element(*OrderPage.station).send_keys(station)
        self.driver.find_element(*OrderPage.click_station).click()
        self.driver.find_element(*OrderPage.phone).send_keys(phone)

    # Кликаем на кнопку "Далее"
    def click_first_form_button_next(self):
        self.driver.find_element(*OrderPage.button_next_1).click()

    # Заполняем вторую страницу формы заказа
    def second_form(self, date, days, color, comment):
        self.driver.find_element(*OrderPage.date).click()
        self.driver.find_element(*OrderPage.date).send_keys(date)
        self.driver.find_element(*OrderPage.dropdown).click()
        self.driver.find_elements(*OrderPage.dropdown_option)[days].click()
        self.driver.find_element(By.ID, color).click()
        self.driver.find_element(*OrderPage.comment).send_keys(comment)

    # Кликаем на кнопку "Далее"
    def click_second_form_button_next(self):
        self.driver.find_element(*OrderPage.button_next_2).click()

    # Кликаем на кнопку "Да"
    def click_button_yes(self):
        self.driver.find_element(*OrderPage.button_window).click()

    # Проверяем сообщение об успешном создании заказа
    def order_window_success(self):
        text = self.driver.find_element(*OrderPage.title_window).text
        return text

    # Кликаем на кнопку "Проверить заказ"
    def button_check_status(self):
        self.driver.find_element(*OrderPage.button_check_status).click()