from pages.main_page import MainPage

def test_main_page(browser):
    link = "https://www.gilmanov.net/"
    page = MainPage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.open_portfolio()  # выполняем метод страницы — переходим на страницу логина
    page.test_buttons()
    page.check_visibility()





