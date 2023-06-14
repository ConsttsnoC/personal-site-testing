#Этот код определяет базовый класс BasePage с методом open(),
# который используется для открытия URL-адреса на веб-странице с помощью предоставленного веб-драйвера.
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
