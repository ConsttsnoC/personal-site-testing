#-> 1) Открытие главной страницы и проверка проверка на наличие резюме после клика по кнопке под фотографией
# на главной странице
#-> 2) Проверка на наличие резюме после клика по кнопке под фотографией на главной странице
from telnetlib import EC

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locat import ButtonsUnderAvatar, NavBar
from pages.base_page import BasePage


class ResumePage(BasePage):
    def test_click_button_resume(self):
        '''Проверка на наличие резюме после клика по кнопке под фотографией на главной странице'''
        button_locator = ButtonsUnderAvatar.RESUME_AVATAR
        button = self.browser.find_element(*button_locator)
        button.click()

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_contains('.pdf'))  # Ожидаем, что URL содержит '/pdf'
        self.browser.back()

    def test_click_navbar_resume(self):
        '''Проверка на наличие резюме после клика по кнопке под фотографией на главной странице'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button_locator = NavBar.RESUME_BUTTON_NAVBAR
        button = self.browser.find_element(*button_locator)
        button.click()
        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_contains('.pdf'))  # Ожидаем, что URL содержит '/pdf'


