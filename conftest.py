#Инициализация работы браузеров "chrome" и "firefox", включение режемов инкогнито


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("-private")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver

    driver.quit()