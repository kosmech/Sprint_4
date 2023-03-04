from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *
from locators.order_page_locators import *

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 6)

    # Ждём загрузки главной страницы
    def wait_load_main_page(self):
        self.wait.until(EC.visibility_of_element_located(MainPage.home_page))

    # Кликаем на кнопку "Заказать" в шапке страницы
    def click_order_button_header(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_middle))
        self.driver.find_element(*MainPage.button_order_header).click()

    # Скроллим страницу до кнопки "Заказать"
    def scroll_button_order_middle(self):
        a = self.driver.find_element(*MainPage.sroll_button_middle)
        self.driver.execute_script('arguments[0].scrollIntoView();', a)
        self.wait.until(EC.visibility_of_element_located(MainPage.sroll_button_middle))
        self.wait.until(EC.element_to_be_clickable(MainPage.button_order_middle))

    # Кликаем на кнопку "Заказать" в середине страницы
    def click_order_button_middle(self):
        self.driver.find_element(*MainPage.button_order_middle).click()

    # Кликаем на кнопку лого Самоката
    def click_logo_scooter(self):
        self.driver.find_element(*MainPage.logo_scooter).click()
        self.wait.until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/'))

    # Кликаем на кнопку лого Яндекса
    def click_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(MainPage.logo_yandex))
        self.driver.find_element(*MainPage.logo_yandex).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    # Ждём загрузки страницы Яндекса
    def wait_load_yandex_search(self):
        self.wait.until(EC.url_to_be('https://dzen.ru/?yredirect=true'))