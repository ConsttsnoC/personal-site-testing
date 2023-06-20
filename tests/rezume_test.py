
from pages.rezume_page import RezumePage

def test_rezume(browser):
    link = "https://www.gilmanov.net/"
    page = RezumePage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.test_ckick_button_rezume()
    page.test_ckick_navbar_rezume()



