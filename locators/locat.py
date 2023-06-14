from selenium.webdriver.common.by import By

class GithubPageLocators:
    GITHUB_BUTTON = (By.CSS_SELECTOR,'img[src="https://img.icons8.com/ios-glyphs/30/null/github.png"]')

#Локаторы для иконок контактов соц.сетей в шапке
class NavBar:
    GLAVNAYA_BUTTON_NAVBAR = (By.CSS_SELECTOR,'a.nav-link.active.font-weight-bold[aria-current="page"][href="/"]')
    PORTFOLIO_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.nav-link.active.font-weight-bold[aria-current="page"][href="/blog/"]')
    REZUME_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.nav-link.font-weight-bold[href="/static/portfolio/%D0%93%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%20%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD.pdf"]')
    GITHUB_BUTTON_NAVBAR = (By.XPATH, '//img[@src="https://img.icons8.com/ios-glyphs/30/null/github.png"]')
    INSTAGRAM_BUTTON_NAVBAR = (By.XPATH, '//img[@src="https://img.icons8.com/ios-glyphs/30/null/instagram-new.png"]')
    VK_BUTTON_NAVBAR = (By.XPATH,'//img[@src="https://img.icons8.com/ios-glyphs/30/null/vk-circled.png"]')
    TELEGRAM_BUTTON_NAVBAR = (By.XPATH,'//img[@src="https://img.icons8.com/ios-glyphs/30/null/filled-sent.png"]')
    KONSTANTIN_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'a.navbar-brand')
    LOGO_IMAGE_BUTTON_NAVBAR = (By.CSS_SELECTOR, 'img.d-inline-block.align-text-top')

#Локаторы для кнопок под Аватаром
class ButtonsUnderAvatar:
    #Кнопка портфолио
    PORTFOLIO_AVATAR = (By.XPATH, '//a[@class="btn btn-secondary m-2" and @href="/blog/"]')
    REZUME_AVATAR = (By.CSS_SELECTOR, 'a.btn.btn-secondary.m-2[href="/static/portfolio/%D0%93%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%20%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD.pdf"]')
    GITHUB_AVATAR = (By.XPATH, "//a[@href='https://github.com/ConsttsnoC?tab=repositories']")










