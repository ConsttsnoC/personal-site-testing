

from selenium.webdriver.common.by import By

#Локаторы для иконок контактов соц.сетей в шапке
class NavBar:
    #Главаня
    HOME_BUTTON_NAVBAR = (By.CSS_SELECTOR,'a.nav-link.active.font-weight-bold[aria-current="page"][href="/"]')
    #Портфолио
    PORTFOLIO_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.nav-link.active.font-weight-bold[aria-current="page"][href="/blog/"]')
    #Резюме
    RESUME_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.nav-link.font-weight-bold[href="/static/portfolio/%D0%93%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%20%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD.pdf"]')
    #GitHub
    GITHUB_BUTTON_NAVBAR = (By.XPATH, '//img[@src="https://img.icons8.com/ios-glyphs/30/null/github.png"]')
    #instagram
    INSTAGRAM_BUTTON_NAVBAR = (By.XPATH, '//img[@src="https://img.icons8.com/ios-glyphs/30/null/instagram-new.png"]')
    #vk
    VK_BUTTON_NAVBAR = (By.XPATH,'//img[@src="https://img.icons8.com/ios-glyphs/30/null/vk-circled.png"]')
    #telegram
    TELEGRAM_BUTTON_NAVBAR = (By.XPATH,'//img[@src="https://img.icons8.com/ios-glyphs/30/null/filled-sent.png"]')
    #Константин Гильманов
    KONSTANTIN_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.navbar-brand')
    #Иконка питона
    LOGO_IMAGE_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'img.d-inline-block.align-text-top')

#Локаторы для кнопок под Аватаром
class ButtonsUnderAvatar:
    #Кнопка портфолио
    PORTFOLIO_AVATAR = (By.XPATH, '//a[@class="btn btn-secondary m-2" and @href="/blog/"]')
    #Резюме
    RESUME_AVATAR = (By.CSS_SELECTOR, 'a.btn.btn-secondary.m-2[href="/static/portfolio/%D0%93%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%20%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD.pdf"]')
    #GitHub
    GITHUB_AVATAR = (By.XPATH, "//a[@href='https://github.com/ConsttsnoC?tab=repositories']")

class TaskTestCreate:
    #кнопка "Начать" на главной "Task"
    BUTTON_BEGIN = (By.CSS_SELECTOR,'a.btn.btn-primary.btn-lg')


#Переход в приложения со страницы портфолио
class RedirectButtons:
    #Кнопка для перехода в приложение агрегатора паролей
    BUTTON_TASK = (By.XPATH, '//a[@href="https://taskksat.pythonanywhere.com/"]')
    #Кнопка для перехода в приложение Задачи
    PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a.btn.btn-secondary[href="https://www.gilmanov.net/parol/"]')












