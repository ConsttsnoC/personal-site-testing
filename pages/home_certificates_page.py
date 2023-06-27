#->1) Проверка отображения картинок сертификатов на главной странице
#->2) Проверка на отображение аватара и текста под ним
#->3) Проверка на отображение текста под сертификатами
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os


class HomeCertificates(BasePage):

    def check_certificate_images(self):
        '''Проверка отображения картинок сертификатов на главной странице'''

        elements = self.browser.find_elements(By.XPATH, '//img[@class="card-img-top"]')
        screenshots = []

        for index, element in enumerate(elements):
            if element.is_displayed():
                print("Элемент сертификата отображается корректно.")
            else:
                print("Элемент сертификата не отображается корректно.")
                # Сохранение скриншота для невидимых элементов
                screenshot_path = os.path.join("C:\\qatest\\screenshots", f"element_{index}.png")
                element.screenshot(screenshot_path)
                screenshots.append(screenshot_path)

        return screenshots

    def check_avatar(self):
        '''Проверка на отображение аватара и текста под ним'''
        element = self.browser.find_element(By.XPATH, '//div[@class="container px-2 text-center"]')

        screenshots = []

        if element.is_displayed():
            print("Элемент аватара отображается корректно.")
        else:
            print("Элемент аватара не отображается корректно.")
            # Сохранение скриншота, если элемент не отображается
            screenshot_path = os.path.join("C:\\qatest\\screenshots", "avatar.png")
            element.screenshot(screenshot_path)
            screenshots.append(screenshot_path)

        return screenshots

    def check_certificate_text(self):
        '''Проверка на отображение текста под сертификатами '''
        elements = self.browser.find_elements(By.XPATH, '//div[@class="text-center"]')
        screenshots = []

        for index, element in enumerate(elements):
            if element.is_displayed():
                text = element.text
                print(f"Текст сертификата {index + 1}: '{text}' отображается корректно.")
            else:
                print(f"Текст сертификата {index + 1} не отображается корректно.")
                screenshot_path = os.path.join("C:\\qatest\\screenshots", f"element_{index}.png")
                element.screenshot(screenshot_path)
                screenshots.append(screenshot_path)

        return screenshots