from pages.home_certificates_page import HomeCertificates

def test_certificates_page(browser):
    link = "https://www.gilmanov.net/"
    page = HomeCertificates(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.check_certificate_images()
    page.check_avatar()
    page.check_certificate_text()
