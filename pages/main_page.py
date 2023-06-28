#тест-кейс: 1)Открытие главной страницы -> 2)Переход на страницу Портфолио по кнопке под аватаркой на главной странице ->
#-> 3)Проверка кнопок "Посмотреть сайт" затем проверка кнопок "Посмотреть код" (сравниваются ожидаемые url)
#-> 4)Проверка отображение картинок сайтов

import os
import time
from selenium.webdriver.common.by import By
from locators.locat import ButtonsUnderAvatar
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def open_portfolio(self):
        '''Нажатие на кнопку ПОРТФОЛИО под фотографией на главной странице'''
        wait = WebDriverWait(self.browser, 10)
        button = wait.until(EC.element_to_be_clickable(ButtonsUnderAvatar.PORTFOLIO_AVATAR))
        button.click()


    def test_buttons(self):
        '''Проверка кнопок "Посмотреть сайт" и "Посмотреть код на странице портфолио, проверка на ожидаемый переход URL"'''
        button_urls = [
            ('https://taskksat.pythonanywhere.com/', '//a[@href="https://taskksat.pythonanywhere.com/"]'),
            ('https://github.com/ConsttsnoC/django-task', '//a[@href="https://github.com/ConsttsnoC/django-task"]'),]
        for expected_url, xpath in button_urls:
            button = self.browser.find_element(By.XPATH, xpath)
            button.click()

            # Явное ожидание загрузки страницы
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.url_contains(expected_url))

            new_url = self.browser.current_url

            try:
                assert expected_url == new_url
                print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
            except AssertionError:
                print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

            self.browser.back()  # Возврат на предыдущую страницу
            self.browser.execute_script("window.scrollBy(0, window.innerHeight * 0.25);")
            time.sleep(1)  # Дайте странице время для прокрутки



    def test_buttons_password_generate(self):
        '''Проверка кнопок "Посмотреть сайт" и "Посмотреть код на странице портфолио, проверка на ожидаемый переход URL"'''
        button_urls = [
            ('https://www.gilmanov.net/parol/', '//a[@href="https://www.gilmanov.net/parol/"]'),
            ('https://github.com/ConsttsnoC/Django3_Password_generate','//a[@href="https://github.com/ConsttsnoC/Django3_Password_generate"]'),]
        for expected_url, xpath in button_urls:
            button = self.browser.find_element(By.XPATH, xpath)
            button.click()

            # Явное ожидание загрузки страницы
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.url_contains(expected_url))

            new_url = self.browser.current_url

            try:
                assert expected_url == new_url
                print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
            except AssertionError:
                print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

            self.browser.back()  # Возврат на предыдущую страницу
            self.browser.execute_script("window.scrollBy(0, window.innerHeight * 0.25);")
            time.sleep(1)  # Дайте странице время для прокрутки

    def test_buttons_rsu(self):
        '''Проверка кнопок "Посмотреть сайт" и "Посмотреть код на странице портфолио, проверка на ожидаемый переход URL"'''
        button_urls = [
            ('https://rsu69.pythonanywhere.com/', '//a[@href="https://rsu69.pythonanywhere.com/"]'),
            ('https://github.com/ConsttsnoC/rsu-69', '//a[@href="https://github.com/ConsttsnoC/rsu-69"]'), ]
        for expected_url, xpath in button_urls:
            button = self.browser.find_element(By.XPATH, xpath)
            button.click()

            # Явное ожидание загрузки страницы
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.url_contains(expected_url))

            new_url = self.browser.current_url

            try:
                assert expected_url == new_url
                print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
            except AssertionError:
                print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

            self.browser.back()  # Возврат на предыдущую страницу
            self.browser.execute_script("window.scrollBy(0, window.innerHeight * 0.25);")
            time.sleep(1)  # Дайте странице время для прокрутки

    def test_buttons_stripeapi(self):
        '''Проверка кнопок "Посмотреть сайт" и "Посмотреть код на странице портфолио, проверка на ожидаемый переход URL"'''
        button_urls = [
            ('https://stripeapi.pythonanywhere.com/', '//a[@href="https://stripeapi.pythonanywhere.com/"]'),
            ('https://github.com/ConsttsnoC/ConsttsnoC-Django-StripeAPI','//a[@href="https://github.com/ConsttsnoC/ConsttsnoC-Django-StripeAPI"]') ]
        for expected_url, xpath in button_urls:
            button = self.browser.find_element(By.XPATH, xpath)
            button.click()

            # Явное ожидание загрузки страницы
            wait = WebDriverWait(self.browser, 10)
            wait.until(EC.url_contains(expected_url))

            new_url = self.browser.current_url

            try:
                assert expected_url == new_url
                print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
            except AssertionError:
                print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

            self.browser.back()  # Возврат на предыдущую страницу
            self.browser.execute_script("window.scrollBy(0, window.innerHeight * 0.25);")
            time.sleep(1)  # Дайте странице время для прокрутки


    def check_visibility(self):
        '''Проверка видимости каждого элемента и сохранение скриншота для невидимых элементов'''
        elements = self.browser.find_elements(By.XPATH, '//img[@class="card-img-top"]')

        screenshots = []
        wait = WebDriverWait(self.browser, 10)
        for index, element in enumerate(elements):
            if wait.until(EC.visibility_of(element)):
                print("Элемент картинки отображается корректно.")
            else:
                print("Элемент картинки не отображается корректно.")
                screenshot_path = os.path.join("C:\\qatest\\screenshots", f"element_{index}.png")
                element.screenshot(screenshot_path)
                screenshots.append(screenshot_path)

        return screenshots


















