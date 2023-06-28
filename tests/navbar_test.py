from pages.navbar_page import NavBarPage

def test_navbar_page(browser):
    link = "https://www.gilmanov.net/"
    page = NavBarPage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.open_home_navbar()
    page.test_buttons_navbar_github()
    page.test_buttons_navbar_instagram()
    page.test_buttons_navbar_vk()
    page.test_buttons_navbar_telegram()
    page.open_portfolio_navbar()
    page.test_home_icon()
    page.test_home()


