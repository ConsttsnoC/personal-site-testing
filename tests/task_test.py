from pages.task_page import TaskPage


def test_rezume(browser):
    link = "https://www.gilmanov.net/"
    page = TaskPage(browser, link)  # инициализируем Page Object с chrome_browser
    page.open()  # открываем страницу
    page.test_open_task()
    page.start_task()
    page.entrance()
    page.creating_a_task()