from selenium.webdriver.common.by import By

class MainPage:

    home_page = (By.CLASS_NAME, 'Home_HomePage__ZXKIX')
    questions = (By.CLASS_NAME, 'accordion')

    # Вопросы
    questions_0 = (By.ID, 'accordion__heading-0')
    questions_1 = (By.ID, 'accordion__heading-1')
    questions_2 = (By.ID, 'accordion__heading-2')
    questions_3 = (By.ID, 'accordion__heading-3')
    questions_4 = (By.ID, 'accordion__heading-4')
    questions_5 = (By.ID, 'accordion__heading-5')
    questions_6 = (By.ID, 'accordion__heading-6')
    questions_7 = (By.ID, 'accordion__heading-7')

    # Ответы
    answer_0 = (By.ID, 'accordion__panel-0')
    answer_1 = (By.ID, 'accordion__panel-1')
    answer_2 = (By.ID, 'accordion__panel-2')
    answer_3 = (By.ID, 'accordion__panel-3')
    answer_4 = (By.ID, 'accordion__panel-4')
    answer_5 = (By.ID, 'accordion__panel-5')
    answer_6 = (By.ID, 'accordion__panel-6')
    answer_7 = (By.ID, 'accordion__panel-7')

    # Кнопки
    button_order_header = (By.XPATH, "(//button[text()='Заказать'])[1]")
    sroll_button_middle = (By.CLASS_NAME, 'Home_FinishButton__1_cWm')
    button_order_middle = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Логотипы
    logo_scooter = (By.XPATH, "//*[@alt='Scooter']")
    logo_yandex = (By.XPATH, "//*[@alt='Yandex']")