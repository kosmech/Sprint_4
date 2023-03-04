from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import *


class Questions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    # Кликаем на вопрос
    def click_question(self, question):
        self.wait.until(EC.visibility_of_element_located(question))
        a = self.driver.find_element(*question)
        self.driver.execute_script('arguments[0].scrollIntoView();', a)
        self.wait.until(EC.visibility_of_element_located(question))
        self.wait.until(EC.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    # Проверяем текст вопросов
    def text_answer(self, answer):
        return self.driver.find_element(*answer).text


class ButtonsOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    def click_button_order_header(self, button):
        self.driver.find_element(*button).click()