# -*- coding: utf-8 -*-
from pages.home_certificates_page import HomeCertificates

def test_github_page(browser):
    link = "https://www.gilmanov.net/"
    page = HomeCertificates(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.home_certificates()
    page.home_avatar()
    page.home_certificates_text()
