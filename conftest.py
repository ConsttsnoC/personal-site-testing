#Инициализация работы браузеров "chrome" и "firefox", включение режемов инкогнито
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# @pytest.fixture(params=["chrome", "firefox"])
# def browser(request):
#     if request.param == "chrome":
#         options = Options()
#         options.add_argument("--incognito")
#         options.add_argument("--start-maximized")  # Add this line to maximize the window
#         options.add_argument("--headless")  # Add this line to run in headless mode
#         driver = webdriver.Chrome(options=options)
#         driver.maximize_window()  # Add this line to maximize the window
#     elif request.param == "firefox":
#         options = FirefoxOptions()
#         options.add_argument("-private")
#         options.add_argument("--start-maximized")  # Add this line to maximize the window
#         options.add_argument("-headless")  # Add this line to run in headless mode
#         driver = webdriver.Firefox(options=options)
#         driver.maximize_window()  # Add this line to maximize the window
#     else:
#         raise ValueError(f"Unsupported browser: {request.param}")
#
#     yield driver
#
#     driver.quit()

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()