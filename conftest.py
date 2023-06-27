#Инициализация работы браузеров "chrome" и "firefox", включение режемов инкогнито


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()