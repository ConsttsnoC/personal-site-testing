from pages.github_page import GithubPage

def test_github_page(browser):
    link = "https://www.gilmanov.net/"
    page = GithubPage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.test_github_navbar()  # выполняем метод страницы — переходим на страницу логина
    page.test_github_avatar()


