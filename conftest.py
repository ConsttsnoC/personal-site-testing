#Инициализация работы браузеров "chrome" и "firefox", включение режемов инкогнито


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")  # Add this line to maximize the window
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()