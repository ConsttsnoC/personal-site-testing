
from pages.base_page import BasePage
from locators.locat import NavBar, ButtonsUnderAvatar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GithubPage(BasePage):
    def test_github_navbar(self):
        '''Открытия Github по клику кнопки в Navbar и проверка на url'''
        button = self.browser.find_element(*NavBar.GITHUB_BUTTON_NAVBAR)
        button.click()


        # Переключаемся на новую вкладку
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_to_be('https://github.com/ConsttsnoC?tab=repositories'))

        new_url = self.browser.current_url
        expected_url = 'https://github.com/ConsttsnoC?tab=repositories'

        try:
            assert expected_url == new_url
            print("Открыт правильный сайт GitHub из Шапки.")
        except AssertionError:
            print(f"Открыт неправильный сайт из Шапки. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")

        # Закрыть текущую вкладку
        self.browser.close()

        # Переключиться на предыдущую вкладку
        self.browser.switch_to.window(self.browser.window_handles[0])


    def test_github_avatar(self):
        '''Открытия Github по клику кнопки под аватаром и проверка на url'''
        button = self.browser.find_element(*ButtonsUnderAvatar.GITHUB_AVATAR)
        button.click()

        # Переключаемся на новую вкладку
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Явное ожидание загрузки страницы
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_to_be('https://github.com/ConsttsnoC?tab=repositories'))

        new_url = self.browser.current_url
        expected_url = 'https://github.com/ConsttsnoC?tab=repositories'

        try:
            assert expected_url == new_url
            print("Открыт правильный сайт GitHub. Под Аватаром.")
        except AssertionError:
            print(f"Открыт неправильный сайт. Под Аватаром. Ожидаемый URL: {expected_url}. Текущий URL: {new_url}.")


