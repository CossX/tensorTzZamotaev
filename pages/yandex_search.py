from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.common import Common


class YandexSearch(Common):

    # Иконка в меню сервисов на странице Яндекс
    def element_services_icon(self, icon_name):
        return self.driver.find_element(By.XPATH, self.YANDEX_SEARCH_IMAGE_ICON.format(icon_name))

    # Проверяет, что список с подсказками (suggest) отобразился
    def check_suggest_is_displayed(self):
        css_value = self.driver.find_element(By.XPATH, self.YANDEX_SEARCH_SUGGEST).value_of_css_property("display")
        if css_value == "block":
            check_suggest = True
        else:
            print("Элемент 'suggest' не отобразился")
            check_suggest = False
        assert check_suggest

    # Нажимает ENTER и проверяет. что появились результаты поиска
    def click_enter_and_check_search_table(self):
        self.element_search_field().send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.YANDEX_SEARCH_RESULT_TABLE).is_displayed()

    # Собирает список ссылок из первых пяти результатов поиска и проверяет, что в нем есть искомая ссылка
    def check_link_in_result(self, expected_link_text):
        link_list = []
        for i in range(1, 6):
            actual_link_text = self.driver.find_element(By.XPATH, f"//ul[@id='search-result']//li[{i}]//a[contains(@class, 'Link_theme_outer')]").text
            link_list.append(actual_link_text)
        if expected_link_text not in link_list:
            print(f"В пяти первых результатах поисковой выдачи ссылки '{expected_link_text}' нет")
        assert expected_link_text in link_list

    # Нажимает на иконку в меню сервисов на странице Яндекс
    def click_on_services_icon(self, icon_name):
        self.element_services_icon(icon_name).click()
