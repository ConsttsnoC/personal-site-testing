#1) test_open_task(Переход с главной страницы на страницу Портфолио -> переход с Портфолио на сайт Task->)
#2) start_task(Клин на кнопку "Начать" -> Заполнение формы регистрации-> Регистрация и Выход на основную страницу Task)
#3) entrance (Нажатие кнопки "Войти" -> заполнение имени и пароля -> очищение полей -> запонение полей -> Вход на сайт)
#4)
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
from pages.base_page import BasePage
from locators.locat import ButtonsUnderAvatar, TaskTestCreate, RedirectButtons
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore
# Инициализация модуля colorama
init()
class TaskPage(BasePage):

    def start_task(self):
        # кнопка "Начать" на главной "Task"
        button = self.browser.find_element(*TaskTestCreate.BUTTON_BEGIN)
        button.click()
        # Проверка перехода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print(Fore.GREEN + 'Переход на сайт TASK РЕГИСТРАЦИЯ выполнен успешно.')
        else:
            print(Fore.RED + 'Переход на сайт не выполнен.')

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

        # Находим кнопку Регистрация
        button_element = self.browser.find_element(By.CLASS_NAME, 'btn-primary')
        # Нажимаем на элемент
        button_element.click()
        # Проверка перехода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print(Fore.GREEN + 'Переход на сайт И РЕГИСТРАЦИЯ выполнена успешно.')
        else:
            print(Fore.RED + 'Переход на сайт не выполнен.')

         # Находим элемент Выход
        button_element = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-dark')
        # Нажимаем на элемент
        button_element.click()\

        # Проверка выхода на нужный сайт
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/':
            print(Fore.GREEN + 'Выход с сайта выполнен успешно.')
        else:
            print(Fore.RED + 'Выход с сайта не выполнен.')

    def entrance(self):
        #клик по кнопке регистрации в NavBar
        link_element = self.browser.find_element(By.LINK_TEXT, 'Зарегистрироваться')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print(Fore.GREEN + 'Переход на страницу РЕГИСТРАЦИЯ выполнена успешно.')
        else:
            print(Fore.RED + 'Переход на сайт не выполнен.')
        self.browser.back()  # Возврат на предыдущую страницу
        #клик по кнопке войти
        link_element = self.browser.find_element(By.LINK_TEXT, 'Войти')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/login/':
            print(Fore.GREEN + 'Переход на страницу Вход выполнена успешно.')
        else:
            print(Fore.RED + 'Переход на сайт не выполнен.')
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
            print(Fore.GREEN + 'Поля имени и пароля очищены.')
        else:
            print(Fore.RED + 'Поля имени и пароля НЕ очищены.')

        link_element = self.browser.find_element(By.LINK_TEXT, 'Регистрация')
        link_element.click()
        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/signup/':
            print(Fore.GREEN + 'Переход по кнопке "регистрация" выполнен успешно.')
        else:
            print(Fore.RED + 'Переход по кнопке "регистрация" не выполнен.')
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
            print(Fore.GREEN + 'Вход выполнен успешно.')
        else:
            print(Fore.RED + 'Вход на сайт не выполнен.')

    def creating_a_task(self):
        # Ожидание появления элемента
        wait = WebDriverWait(self.browser, 10)
        link_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'btn btn-primary')]")))

        # Нажатие на элемент
        link_element.click()
        wait.until(EC.url_to_be('https://taskksat.pythonanywhere.com/create/'))

        input_element = wait.until(EC.element_to_be_clickable((By.ID, "title")))
        input_element.send_keys('Первое название')
        input_element = wait.until(EC.element_to_be_clickable((By.ID, "memo")))
        input_element.send_keys('Первое описание')
        checkbox = wait.until(EC.element_to_be_clickable((By.ID, 'important')))
        checkbox.click()
        elements = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))
        elements.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print(Fore.GREEN + 'сохранение выполнено успешно.')
        else:
            print(Fore.RED + 'сохранение не выполнено.')


        # Нажатие на кнопку с атрибутом "aria-label" равным "Выполнение задачи" и значением "✓"
        buttons = self.browser.find_elements(By.XPATH,
                                             "//button[contains(@aria-label, 'Выполнение задачи') and contains(text(), '✓')]")
        if len(buttons) >= 1:
            buttons[-1].click()
            print(Fore.GREEN + "Задание выполнено.")

        # Переход к редактированию задания
        button = self.browser.find_element(By.XPATH,
                                           "//button[contains(@class, 'btn btn-primary') and contains(text(), '✎')]")
        button.click()

        button = self.browser.find_element(By.XPATH, "//button[@class='btn btn-danger' and text()='Удалить']")
        self.browser.execute_script("arguments[0].click();", button)
        time.sleep(2)


        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/completet/':
            print(Fore.GREEN + 'Задание удалено.')
        else:
            print(Fore.RED + 'Задание не удалено.')


    def test_navbar_task(self):
        '''тестирование кнопок navbar'''
        # нажатие кнопки "TASK"
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="navbar-brand" and text()="Task"]')))
        link.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/':
            print(Fore.GREEN + 'переход по кнопке TASK в шапке выполнен успешно.')
        else:
            print(Fore.RED + 'переход по кнопке TASK в шапке НЕ выполнено.')

        # нажатие на кнопку "создать" в NavBar
        # Ожидание появления элемента
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        span_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.navbar-toggler")))

        # Нажатие на элемент
        span_element.click()
        wait = WebDriverWait(self.browser, 10)
        link_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.nav-link[href="/create/"]')))
        link_element.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/create/':
            print(Fore.GREEN + 'переход по кнопке СОЗДАТЬ в шапке выполнен успешно.')
        else:
            print(Fore.RED + 'переход по кнопке СОЗДАТЬ в шапке НЕ выполнено.')


        # нажатие на кнопку "Текущие"
        # Ожидание появления элемента
        wait = WebDriverWait(self.browser, 10)
        span_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.navbar-toggler")))

        # Нажатие на элемент
        span_element.click()
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link active" and text()="Текущие"]')))
        link.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/current/':
            print(Fore.GREEN + 'переход по кнопке ТЕКУЩИЕ в шапке выполнен успешно.')
        else:
            print(Fore.RED + 'переход по кнопке ТЕКУЩИЕ в шапке не выполнено.')

        # нажатие на кнопку Выполненные
        # Ожидание появления элемента
        wait = WebDriverWait(self.browser, 10)
        span_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.navbar-toggler")))

        # Нажатие на элемент
        span_element.click()
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        time.sleep(1)
        wait = WebDriverWait(self.browser, 10)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link" and text()="Выполненные"]')))
        link.click()

        if self.browser.current_url == 'https://taskksat.pythonanywhere.com/completet/':
            print(Fore.GREEN + 'переход по кнопке ВЫПОЛНЕННЫЕ в шапке выполнен успешно.')
        else:
            print(Fore.RED + 'переход по кнопке ВЫПОЛНЕННЫЕ в шапке НЕ выполнено.')











