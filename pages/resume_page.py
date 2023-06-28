#-> 1) Открытие главной страницы и проверка проверка на наличие резюме после клика по кнопке под фотографией
# на главной странице
#-> 2) Проверка на наличие резюме после клика по кнопке под фотографией на главной странице

from locators.locat import ButtonsUnderAvatar, NavBar
from pages.base_page import BasePage


class ResumePage(BasePage):

    def test_click_button_resume(self):
        '''Проверка наличия резюме после клика по кнопке под фотографией на главной странице'''
        # Получение идентификатора текущего окна
        current_window = self.browser.current_window_handle

        # Нажатие на кнопку
        button = self.browser.find_element(*ButtonsUnderAvatar.RESUME_AVATAR)
        button.click()



class ResumePageNav(BasePage):

    def test_click_navbar_resume(self):
        '''Проверка наличия резюме после клика по кнопке в навигационной панели'''
        self.browser.execute_script("window.scrollTo(0, 0)")  # Скроллинг вверх
        button = self.browser.find_element(*NavBar.RESUME_BUTTON_NAVBAR)
        button.click()






