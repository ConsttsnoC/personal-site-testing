import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Убедитесь, что вы установили colorama
from colorama import init, Fore

# Инициализация цветовых стилей для консоли
init(autoreset=True)

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("-private")
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver

    driver.quit()
