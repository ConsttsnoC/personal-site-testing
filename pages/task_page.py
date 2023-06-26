#1) test_open_task(Переход с главной страницы на страницу Портфолио -> переход с Портфолио на сайт Task->)
#2) start_task(Клин на кнопку "Начать" -> Заполнение формы регистрации-> Регистрация и Выход на основную страницу Task)
#3) entrance (Нажатие кнопки "Войти" -> заполнение имени и пароля -> очищение полей -> запонение полей -> Вход на сайт)
#4)

from selenium.webdriver.common.by import By
import random
from pages.base_page import BasePage
from locators.locat import ButtonsUnderAvatar, TaskTestCreate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TaskPage(BasePage):

    def test_open_task(self):
        '''Открытия Портфолио по клику кнопки в кнопки под аватаром и проверка на url'''
        button = self.browser.find_element(*ButtonsUnderAvatar.PORTFOLIO_AVATAR)
        button.click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="https://taskksat.pythonanywhere.com/"]'))
        )
        element.click()
        # Проверка перехода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/':
            print('Переход на сайт TASK выполнен успешно.')
        else:
            print('Переход на сайт не выполнен.')

    def start_task(self):
        # кнопка "Начать" на главной "Task"
        button = self.browser.find_element(*TaskTestCreate.BUTTON_BEGIN)
        button.click()
        # Проверка перехода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print('Переход на сайт TASK РЕГИСТРАЦИЯ выполнен успешно.')
        else:
            print('Переход на сайт не выполнен.')

        # Находим элемент по атрибуту name
        input_element = self.browser.find_element(By.ID, "username")
        # Генерация случайной строки из букв
        cyrillic_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        random_letters = ''.join(random.choice(cyrillic_letters) for _ in range(5))
        # Вводим значение в элемент
        input_element.send_keys(random_letters)
        # Находим элемент по атрибуту name
        password_element = self.browser.find_element(By.ID,'password1')
        # Вводим значение в элемент
        password_element.send_keys('123456')
        password_element_repetition = self.browser.find_element(By.ID,'password2')
        password_element_repetition.send_keys('123456')

        # Находим элемент Выход
        button_element = self.browser.find_element(By.CLASS_NAME, 'btn-primary')
        # Нажимаем на элемент
        button_element.click()
        # Проверка перехода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print('Переход на сайт И РЕГИСТРАЦИЯ выполнена успешно.')
        else:
            print('Переход на сайт не выполнен.')

         # Находим элемент Выход
        button_element = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-dark')
        # Нажимаем на элемент
        button_element.click()\

        # Проверка выхода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/':
            print('Выход с сайта выполнен успешно.')
        else:
            print('Выход с сайта не выполнен.')

    def entrance(self):
        #клик по кнопке регистрации в NavBar
        link_element = self.browser.find_element(By.LINK_TEXT, 'Зарегистрироваться')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print('Переход на страницу РЕГИСТРАЦИЯ выполнена успешно.')
        else:
            print('Переход на сайт не выполнен.')
        self.browser.back()  # Возврат на предыдущую страницу
        #клик по кнопке войти
        link_element = self.browser.find_element(By.LINK_TEXT, 'Войти')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/login/':
            print('Переход на страницу Вход выполнена успешно.')
        else:
            print('Переход на сайт не выполнен.')
        #заполнение формы входа
        input_element = self.browser.find_element(By.ID, "username")
        input_element.send_keys('ккк')
        input_element = self.browser.find_element(By.ID, "password")
        input_element.send_keys('123456')
        #очищение полей с помощью нажатия кнопки "Сбросить"
        elements = self.browser.find_element(By.CSS_SELECTOR, 'input[type="reset"]')
        elements.click()

        # Проверка, что поля стали пустыми
        username_input = self.browser.find_element(By.ID, "username")
        password_input = self.browser.find_element(By.ID, "password")

        if username_input.get_attribute("value") == '' and password_input.get_attribute("value") == '':
            print('Поля имени и пароля очищены.')
        else:
            print('Поля имени и пароля НЕ очищены.')

        link_element = self.browser.find_element(By.LINK_TEXT, 'Регистрация')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print('Переход по кнопке "регистрация" выполнен успешно.')
        else:
            print('Переход по кнопке "регистрация" не выполнен.')
        self.browser.back()  # Возврат на предыдущую страницу
        # заполнение формы входа
        input_element = self.browser.find_element(By.ID, "username")
        input_element.send_keys('ккк')
        input_element = self.browser.find_element(By.ID, "password")
        input_element.send_keys('123456')
        #Нажатие кнопки Вход
        button_element = self.browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[type="submit"]')
        button_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print('Вход выполнен успешно.')
        else:
            print('Вход на сайт не выполнен.')

    def creating_a_task(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        link_element = self.browser.find_element(By.XPATH, "//a[contains(@class, 'btn-primary')]")
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/create/':
            print('переход на создание выполнен успешно.')
        else:
            print('переход на создание не выполнен.')

        input_element = self.browser.find_element(By.ID, "title")
        input_element.send_keys('Первое название')
        input_element = self.browser.find_element(By.ID, "memo")
        input_element.send_keys('Первое описание')
        elements = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        elements.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print('сохранение выполнено успешно.')
        else:
            print('сохранение не выполнено.')

        # Нажатие на кнопку с атрибутом "aria-label" равным "Выполнение задачи" и значением "✓"
        buttons = self.browser.find_elements(By.XPATH,
                                             "//button[contains(@aria-label, 'Выполнение задачи') and contains(text(), '✓')]")
        if len(buttons) >= 1:
            buttons[-1].click()
            print("Задание выполнено.")

        #переход к редактированию задания
        button = self.browser.find_element(By.XPATH,
                                           "//button[contains(@class, 'btn btn-primary') and contains(text(), '✎')]")
        button.click()
        #удаление выполненого задания
        button = self.browser.find_element(By.XPATH,
                                           "//button[contains(@class, 'btn btn-danger') and contains(text(), 'Удалить')]")
        button.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/completet/':
            print('Задание удаленно.')
        else:
            print('Задание не удаленно.')

        #нажатие на кнопку "создать" в NavBar
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        wait = WebDriverWait(self.browser, 10)
        link_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="/create/"]')))
        link_element.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/create/':
            print('переход по кнопке создание в шапке выполнен успешно.')
        else:
            print('переход по кнопке создание в шапке не выполнено.')













