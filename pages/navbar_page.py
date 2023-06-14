#Тест кейс: 1) Проверка работоспособности кнопки портфолио в Navbar ->
#-> 2)Проверка работоспособности кнопки Резюме в Navbar и кнопки Главная ->
#-> 3)Проверка иконок с сылками на контакты соцсетей с проверкой url
#-> 4) Проверка на работоспособность элемента Константин Гильманов в Navbar(переход на главную страницу)
#-> 5) Проверка на работоспособность элемента ИКОНКИ рядом с Константин Гильманов в Navbar(переход на главную страницу)

from selenium.webdriver.common.by import By
from locators.locat import NavBar
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavBarPage(BasePage):
    def open_portfolio_navbar(self):
        '''Проверка кнопки портфолио в Navbar'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.PORTFOLIO_BUTTON_NAVBAR)
        button.click()

        expected_url = 'https://www.gilmanov.net/blog/'  # Ожидаемый URL портфолио
        actual_url = self.browser.current_url

        assert actual_url == expected_url, f"Открылся неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {actual_url}"
        self.browser.back()

    def open_rezume_navbar(self):
        '''Проверка кнопки Резюме в Navbar и кнопки Главная'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.REZUME_BUTTON_NAVBAR)
        button.click()

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_contains('.pdf'))  # Ожидаем, что URL содержит '/resume'

        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх

        button = self.browser.find_element(By.LINK_TEXT, 'Главная')
        button.click()

    def test_button_navbar(self, button_xpath, expected_url):
        '''Проверка иконок с ссылками на контакты соцсетей с проверкой URL'''
        button = self.browser.find_element(By.XPATH, button_xpath)
        button.click()

        # Явное ожидание появления нового окна
        wait = WebDriverWait(self.browser, 10)
        #ожидания, пока количество открытых окон браузера не станет равным 2.
        wait.until(EC.number_of_windows_to_be(2))

        # Переключение на новое окно
        current_window = self.browser.current_window_handle
        windows = self.browser.window_handles
        new_window = [window for window in windows if window != current_window][0]
        self.browser.switch_to.window(new_window)

        # Явное ожидание загрузки страницы
        wait.until(EC.url_to_be(expected_url))
        new_url = self.browser.current_url

        try:
            assert expected_url == new_url
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        except AssertionError:
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

    def test_glav(self):
        '''Проверка на работоспособность элемента Константин Гильманов в Navbar(переход на главную страницу)'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.PORTFOLIO_BUTTON_NAVBAR)
        button.click()
        '''Проверка на работоспособность элемента Константин Гильманов в Navbar'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        wait = WebDriverWait(self.browser, 10)  # Инициализация объекта WebDriverWait
        button = wait.until(
            EC.element_to_be_clickable(NavBar.KONSTANTIN_BUTTON_NAVBAR))  # Ожидание кликабельности кнопки
        button.click()

        new_url = self.browser.current_url
        expected_url = 'https://www.gilmanov.net/'

        try:
            assert expected_url == new_url
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        except AssertionError:
            error_message = f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}."
            self.write_error(error_message)
        self.browser.back()  # Возврат на предыдущую страницу

    def test_glav_icon(self):
        '''Проверка на работоспособность элемента ИКОНКИ рядом с Константин Гильманов в Navbar(переход на главную страницу)'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.PORTFOLIO_BUTTON_NAVBAR)
        button.click()
        '''Проверка на работоспособность элемента ICON в Navbar'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.LOGO_IMAGE_BUTTON_NAVBAR)
        button.click()

        new_url = self.browser.current_url
        expected_url = 'https://www.gilmanov.net/'

        try:

            assert expected_url == new_url
            print(f"Открыт правильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")
        except AssertionError:
            print(f"Открыт неправильный сайт. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")










