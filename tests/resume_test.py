
from pages.resume_page import ResumePage

def test_resume(browser):
    link = "https://www.gilmanov.net/"
    page = ResumePage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу





