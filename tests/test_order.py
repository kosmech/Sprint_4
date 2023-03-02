
import allure
import pytest
from pages.order_page import Order, User as us
from pages.base_pages import BasePage


class TestOrder:

    @allure.title('Тест заказа по кнопке "Заказать" в шапке страницы')
    def test_order_by_the_order_button_in_the_page_header(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        order = Order(self.driver)
        base_page.click_order_button_header()
        order.first_form(us.firstname_1, us.secondname_1, us.address_1, us.station_1, us.phone_1)
        order.click_first_form_button_next()
        order.second_form(us.date_1, us.days_1, us.color_1, us.comment_1)
        order.click_second_form_button_next()
        order.click_button_yes()
        title = order.order_window_success()
        order.button_check_status()
        assert 'Заказ оформлен' in title

        base_page.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        base_page.click_logo_yandex()
        base_page.wait_load_yandex_search()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Тест заказа по кнопке "Заказать" в середине страницы')
    def test_order_by_the_order_button_in_the_page_middle(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        order = Order(self.driver)
        base_page.scroll_button_order_middle()
        base_page.click_order_button_middle()
        order.first_form(us.firstname_2, us.secondname_2, us.address_2, us.station_2, us.phone_2)
        order.click_first_form_button_next()
        order.second_form(us.date_2, us.days_2, us.color_2, us.comment_2)
        order.click_second_form_button_next()
        order.click_button_yes()
        title = order.order_window_success()
        order.button_check_status()
        assert 'Заказ оформлен' in title

        base_page.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

        base_page.click_logo_yandex()
        base_page.wait_load_yandex_search()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'