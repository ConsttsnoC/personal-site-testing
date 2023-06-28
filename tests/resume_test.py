
from pages.resume_page import ResumePage,ResumePageNav

def test_resume(browser):
    link = "https://www.gilmanov.net/"
    page = ResumePage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.test_click_button_resume()
    link = "https://www.gilmanov.net/"
    page = ResumePageNav(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.test_click_navbar_resume()



