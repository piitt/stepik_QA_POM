from .base_page import BasePage
from .locators import MainPageLocators
# для реализации перехода между страницами
from .login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # переход между страницами
        # инициализируем объект страницы с логином и возвращаем его
        # 1 способ
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), 'Login link is not presented'
