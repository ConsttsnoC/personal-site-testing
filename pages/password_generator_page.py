#тест-кейс: 1)Открытие главной страницы -> 2)Переход на страницу Портфолио по кнопке под аватаркой на главной странице ->
#-> 3)Переход на страницу Генератора Паролей + проверка url ->
#-> 4)Генерация Пароля (проверка на генерацию) и выход назад
#-> 5)Меняет длину и по очереди проверяет чекбоксы и генерируем пароли и выход назад
#-> 6)Обновляем страницу, генерируем стандартный пароль, клик по кнопке Сгенерировать пароль,
#->  проверка отличия старого пароля от нового, клик по кнопке Назад, проверка Url


import random
from selenium.webdriver.support.ui import Select
from locators.locat import ButtonsUnderAvatar, RedirectButtons
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PasswordGeneratorPage(BasePage):

    def go_to_site(self):
        expected_url = 'https://www.gilmanov.net/parol/'


        button = self.browser.find_element(*ButtonsUnderAvatar.PORTFOLIO_AVATAR)
        button.click()

        button = self.browser.find_element(*RedirectButtons.PASSWORD_BUTTON)
        button.click()

        new_url = self.browser.current_url

        if expected_url == new_url:
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        else:
            print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

    def test_site_password(self):
        button = self.browser.find_element(By.CSS_SELECTOR,'input[type="submit"][value="Сгенерировать пароль"].btn.btn-primary')
        button.click()
        expected_text = "Ваш персональный пароль:"
        element = self.browser.find_element(By.CSS_SELECTOR, 'h1.display-5')

        if expected_text in element.text:
            print("Текст успешно отображается на странице")
        else:
            print("Текст не найден на странице")

        self.browser.back()

    def test_site_password_has_letters(self):
        '''
        Меняем длину и по очереди проверяет чекбоксы и генерируем пароли и выход назад
        '''
        self.browser.refresh()
        # Случайно выбираем длину пароля от 6 до 14
        password_length = random.randint(6, 14)

        wait = WebDriverWait(self.browser, 10)
        select_element = wait.until(EC.presence_of_element_located((By.NAME, 'length')))
        select = Select(select_element)
        select.select_by_value(str(password_length))

        option1 = self.browser.find_element(By.CSS_SELECTOR, "[name='Верхний регист']")
        option1.click()

        button = self.browser.find_element(By.CSS_SELECTOR,
                                           'input[type="submit"][value="Сгенерировать пароль"].btn.btn-primary')
        button.click()

        password_element = self.browser.find_element(By.CSS_SELECTOR, 'h2.alert.alert-primary[role="alert"]')
        password = password_element.text
        has_letters = any(char.isalpha() for char in password)
        screenshots = []

        if has_letters:
            print("Пароль содержит Верхний регист")
        else:
            print("Пароль не соответствует требованиям 'Верхний регист'")
            # Сохранение скриншота для видимых элементов
            screenshot_path = "C:\\qatest\\screenshots\\1.png"
            self.browser.save_screenshot(screenshot_path)
            screenshots.append(screenshot_path)

        self.browser.back()
        return screenshots

    def test_site_password_has_digits(self):
        self.browser.refresh()
        # Случайно выбираем длину пароля от 6 до 14
        password_length = random.randint(6, 14)

        wait = WebDriverWait(self.browser, 10)
        select_element = wait.until(EC.presence_of_element_located((By.NAME, 'length')))
        select = Select(select_element)
        select.select_by_value(str(password_length))

        option2 = self.browser.find_element(By.CSS_SELECTOR, "[name='Цифры']")
        option2.click()

        button = self.browser.find_element(By.CSS_SELECTOR,
                                           'input[type="submit"][value="Сгенерировать пароль"].btn.btn-primary')
        button.click()

        password_element = self.browser.find_element(By.CSS_SELECTOR, 'h2.alert.alert-primary[role="alert"]')
        password = password_element.text
        has_digits = any(char.isdigit() for char in password)
        screenshots = []

        if has_digits:
            print("Пароль содержит Цифры")
        else:
            print("Пароль не соответствует требованиям 'Цифры'")
            # Сохранение скриншота для видимых элементов
            screenshot_path = "C:\\qatest\\screenshots\\2.png"
            self.browser.save_screenshot(screenshot_path)
            screenshots.append(screenshot_path)

        self.browser.back()
        return screenshots

    def test_site_password_has_special_chars(self):
        self.browser.refresh()
        # Случайно выбираем длину пароля от 6 до 14
        password_length = random.randint(6, 14)

        wait = WebDriverWait(self.browser, 10)
        select_element = wait.until(EC.presence_of_element_located((By.NAME, 'length')))
        select = Select(select_element)
        select.select_by_value(str(password_length))
        option2 = self.browser.find_element(By.CSS_SELECTOR, "[name='Специальные знаки']")
        option2.click()
        button = self.browser.find_element(By.CSS_SELECTOR,
                                           'input[type="submit"][value="Сгенерировать пароль"].btn.btn-primary')
        button.click()
        password_element = self.browser.find_element(By.CSS_SELECTOR, 'h2.alert.alert-primary[role="alert"]')
        password = password_element.text
        has_special_chars = any(not char.isalnum() for char in password)
        screenshots = []
        if has_special_chars:
            print("Пароль содержит Специальные знаки")
        else:
            print("Пароль не соответствует требованиям 'Специальные знаки'")

            # Сохранение скриншота для видимых элементов
            screenshot_path = "C:\\qatest\\screenshots\\3.png"
            self.browser.save_screenshot(screenshot_path)
            screenshots.append(screenshot_path)

        self.browser.back()
        return screenshots

    def creation_of_a_new(self):
        '''Генерация пароля, создание нового пароля, проверка на создание нового пароля, тест работы кнопки "Назад"'''
        self.browser.refresh()

        # Нажать на кнопку "Сгенерировать пароль"
        generate_button = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[type="submit"][value="Сгенерировать пароль"].btn.btn-primary')))
        generate_button.click()

        # Получить сгенерированный пароль
        password_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.alert.alert-primary')))
        generated_password = password_element.text

        # Нажать на кнопку "Другой пароль"
        change_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Другой пароль')))
        change_button.click()

        # Получить новый сгенерированный пароль
        new_password_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2.alert.alert-primary')))
        new_generated_password = new_password_element.text

        if generated_password != new_generated_password:
            print("Сгенерированный пароль:", generated_password)
            print("Новый сгенерированный пароль:", new_generated_password)
        else:
            raise Exception("Ошибка: Сгенерированный пароль не изменился.")

        # Нажатие на кнопку "Назад"
        button = self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Назад"].btn.btn-primary')
        button.click()

        # Проверка изменения текущей ссылки
        expected_url = 'https://www.gilmanov.net/parol/?'
        if self.browser.current_url == expected_url:
            print("Текущая ссылка успешно сменилась на", expected_url)
        else:
            print("Ошибка: Текущая ссылка не изменилась или не соответствует ожидаемой ссылке", expected_url)















