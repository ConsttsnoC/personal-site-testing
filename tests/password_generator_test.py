from pages.password_generator_page import PasswordGeneratorPage

def test_github_page(browser):
    link = "https://www.gilmanov.net/"
    page = PasswordGeneratorPage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.go_to_site()
    page.test_site_password()
    page.test_site_password_has_letters()
    page.test_site_password_has_digits()
    page.test_site_password_has_special_chars()
    page.creation_of_a_new()