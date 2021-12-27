from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.locators import Locators


class Common(Locators):
    def __init__(self, driver):
        self.driver = driver

    # Открывает главную страницу яндекса
    def open_main_url(self):
        self.driver.get("https://yandex.ru")

    # Поле поиска Яндекс
    def element_search_field(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_SEARCH_FIELD)

    # Вводит текст в поле поиска Яндекса
    def input_text_in_search_field(self, text):
        self.element_search_field().clear()
        self.element_search_field().send_keys(text)

    # Кликает по указанному элементу
    @staticmethod
    def click_element(element):
        element.click()

    # Проверяет, что элемент есть на странице
    @staticmethod
    def check_element_displayed(element):
        check = element.is_displayed()
        assert check

    # Проверяет, что открылась новая вкладка и, что url новый вкладки равен указанному
    def check_new_tab_url(self, expected_url, number_of_tab):
        WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(number_of_tab))
        self.driver.switch_to.window(self.driver.window_handles[number_of_tab - 1])
        actual_url = self.driver.current_url
        assert actual_url == expected_url

