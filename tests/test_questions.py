import allure
import pytest
from pages.main_page import Questions
from pages.base_pages import BasePage
from locators.main_page_locators import *


class TestQuestions:

    @allure.title('Тест 1-го вопроса. Проверка ответа')
    def test_questions_1(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_0)

        assert section_questions.text_answer(MainPage.answer_0) == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Тест 2-го вопроса. Проверка ответа')
    def test_questions_2(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_1)

        assert section_questions.text_answer(MainPage.answer_1) == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Тест 3-го вопроса. Проверка ответа')
    def test_questions_3(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_2)

        assert section_questions.text_answer(MainPage.answer_2) == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Тест 4-го вопроса. Проверка ответа')
    def test_questions_4(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_3)

        assert section_questions.text_answer(MainPage.answer_3) == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Тест 5-го вопроса. Проверка ответа')
    def test_questions_5(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_4)

        assert section_questions.text_answer(MainPage.answer_4) == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Тест 6-го вопроса. Проверка ответа')
    def test_questions_6(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_5)

        assert section_questions.text_answer(MainPage.answer_5) == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Тест 7-го вопроса. Проверка ответа')
    def test_questions_7(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_6)

        assert section_questions.text_answer(MainPage.answer_6) == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Тест 8-го вопроса. Проверка ответа')
    def test_questions_8(self, driver):
        self.driver = driver
        base_page = BasePage(self.driver)
        section_questions = Questions(self.driver)
        base_page.wait_load_main_page()
        section_questions.click_question(MainPage.questions_7)

        assert section_questions.text_answer(MainPage.answer_7) == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'