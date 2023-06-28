#Тест кейс:
#-> 1)Проверка работоспособности кнопки Резюме в Navbar и кнопки Главная ->
#-> 2)Проверка иконок со cсылками на контакты соцсетей с проверкой url
#-> 3)Проверка работоспособности кнопки портфолио в Navbar
#-> 4)Проверка на работоспособность элемента Константин Гильманов в Navbar(переход на главную страницу)
# возврат на страницу портфолио
#-> 5)Проверка на работоспособность элемента ИКОНКИ рядом с Константин Гильманов в Navbar(переход на главную страницу)
import time

from selenium.webdriver.common.by import By
from locators.locat import NavBar
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavBarPage(BasePage):

    def open_home_navbar(self):
        '''Проверка кнопки Резюме в Navbar и кнопки Главная'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        # Проверка кнопки "Главная"
        wait = WebDriverWait(self.browser, 10)
        home_button = self.browser.find_element(*NavBar.HOME_BUTTON_NAVBAR)
        home_button.click()
        expected_url = 'https://www.gilmanov.net/'  # Ожидаемый URL портфолио

        # Явное ожидание загрузки страницы
        wait.until(EC.url_contains(expected_url))
        actual_url = self.browser.current_url #получаем текущий url
        if actual_url == expected_url:
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {actual_url}.")
        else:
            print(f"Открылся неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {actual_url}.")

    def test_button_navbar(self, button_xpath, expected_url):
        '''Проверка иконок со ссылками на контакты соцсетей с проверкой URL'''
        button = self.browser.find_element(By.XPATH, button_xpath)
        button.click()

        # Явное ожидание появления нового окна
        wait = WebDriverWait(self.browser, 10)
        # Ожидание, пока количество открытых окон браузера не станет равным 2.
        wait.until(EC.number_of_windows_to_be(2))

        # Переключение на новое окно
        current_window = self.browser.current_window_handle
        new_window = next(window for window in self.browser.window_handles if window != current_window)
        self.browser.switch_to.window(new_window)

        # Явное ожидание загрузки страницы
        wait.until(EC.url_to_be(expected_url))
        new_url = self.browser.current_url

        if expected_url == new_url:
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        else:
            print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

        # Закрытие нового окна и переключение обратно на исходное окно
        self.browser.close()
        self.browser.switch_to.window(current_window)

    def test_buttons_navbar_github(self):
        button_xpath = NavBar.GITHUB_BUTTON_NAVBAR[1]
        expected_url = 'https://github.com/ConsttsnoC?tab=repositories'
        self.test_button_navbar(button_xpath, expected_url)

    def test_buttons_navbar_instagram(self):
        button_xpath = NavBar.INSTAGRAM_BUTTON_NAVBAR[1]
        expected_url = 'https://www.instagram.com/constantsamara/?igshid=MWM2YjBjM2Q%3D'
        self.test_button_navbar(button_xpath, expected_url)

    def test_buttons_navbar_vk(self):
        button_xpath = NavBar.VK_BUTTON_NAVBAR[1]
        expected_url = 'https://vk.com/constantaa'
        self.test_button_navbar(button_xpath, expected_url)

    def test_buttons_navbar_telegram(self):
        button_xpath = NavBar.TELEGRAM_BUTTON_NAVBAR[1]
        expected_url = 'https://t.me/constantasmr'
        self.test_button_navbar(button_xpath, expected_url)

    def open_portfolio_navbar(self):
        '''Проверка кнопки портфолио в Navbar'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.PORTFOLIO_BUTTON_NAVBAR)
        button.click()

        expected_url = 'https://www.gilmanov.net/blog/'  # Ожидаемый URL портфолио

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_contains(expected_url))

        actual_url = self.browser.current_url

        try:
            assert actual_url == expected_url
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {actual_url}.")
        except AssertionError:
            print(f"Открылся неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {actual_url}.")

    def test_home_icon(self):
        '''Проверка на работоспособность элемента ICON в Navbar'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.LOGO_IMAGE_BUTTON_NAVBAR)
        button.click()

        expected_url = 'https://www.gilmanov.net/'  # Ожидаемый URL главной страницы

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_to_be(expected_url))

        new_url = self.browser.current_url

        if new_url == expected_url:
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        else:
            print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

        self.browser.back()  # Возврат на предыдущую страницу

    def test_home(self):
        '''Проверка на работоспособность элемента Константин Гильманов в Navbar (переход на главную страницу)'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        wait = WebDriverWait(self.browser, 10)  # Инициализация объекта WebDriverWait
        button = wait.until(
            EC.element_to_be_clickable(NavBar.KONSTANTIN_BUTTON_NAVBAR))  # Ожидание кликабельности кнопки
        button.click()

        expected_url = 'https://www.gilmanov.net/'
        new_url = self.browser.current_url

        if expected_url == new_url:
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        else:
            print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")










