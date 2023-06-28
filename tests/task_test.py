from pages.task_page import TaskPage


def test_task(browser):
    link = "https://taskksat.pythonanywhere.com/"
    page = TaskPage(browser, link)  # инициализируем Page Object с браузером
    page.open()  # открываем страницу
    page.start_task()
    page.entrance()
