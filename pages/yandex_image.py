from PIL import Image, ImageChops
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.common import Common


class YandexImage(Common):
    # Ссылка страницы с категориями изображений
    YANDEX_SEARCH_IMAGES_PAGE_LINK = "https://yandex.ru/images/?utm_source=main_stripe_big"
    # Путь для сохранения скриншота первой картинки
    FIRST_IMAGE_PATH = "./resources/first_image.png"
    # Путь для сохранения скриншота для следующего изображения
    SECOND_IMAGE_PATH = "./resources/second_image.png"
    # Путь для сохранения скриншота для предыдущего изображения
    THIRD_IMAGE_PATH = "./resources/third_image.png"

    # Первая категория изображений
    def element_first_image_category(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_IMAGE_FIRST_CATEGORY)

    # Первое изображение  в результате поиска
    def element_first_image(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_IMAGE_FIRST_IMAGE)

    # Открытое изображение
    def element_open_image(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_IMAGE_OPEN_IMAGE)

    # Иконка стрелки вперед на изображении
    def element_next_icon(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_IMAGE_NEXT_ICON)

    # Иконка кнопки назад на изображении
    def element_prev_icon(self):
        return self.driver.find_element(By.XPATH, self.YANDEX_IMAGE_PREV_ICON)

    # Получает тайтл категории изображения, кликает по категории, проверяет, что страница поиска с изображениями
    # загрузилась, проверяет, что текст в поле поиска совпадает с тайтлом категории
    def open_first_image_category_and_check(self):
        image_search_text = self.element_first_image_category().text
        self.click_element(self.element_first_image_category())
        expected_yandex_image_page_title = WebDriverWait(self.driver, 20).until(EC.title_contains(image_search_text))
        assert expected_yandex_image_page_title
        text_in_search_field = self.element_search_field().get_attribute('value')
        assert image_search_text == text_in_search_field

    # Кликает по первому изображению в поиске и проверяет, что оно открылось
    def click_first_image_and_check(self):
        self.click_element(self.element_first_image())
        self.check_element_displayed(self.element_open_image())

    # Сравнивает два изображения
    @staticmethod
    def image_compare(img_1, img_2):
        image_1 = Image.open(img_1)
        image_2 = Image.open(img_2)
        dif = ImageChops.difference(image_1, image_2)
        result = np.mean(np.array(dif))
        if result < 0.15:
            return True
        else:
            return False

    # Кликает на иконку вперед на изобрражении, проверяет, что картинка поменялась
    def click_next_and_check_image(self):
        self.element_open_image().screenshot(self.FIRST_IMAGE_PATH)
        self.click_element(self.element_next_icon())
        self.check_element_displayed(self.element_open_image())
        self.element_open_image().screenshot(self.SECOND_IMAGE_PATH)
        result = self.image_compare(self.FIRST_IMAGE_PATH, self.SECOND_IMAGE_PATH)
        assert not result

    # Кликает на иконку назад на изобрражении, проверяет, что картинка таже, что и была
    def click_prev_and_check_image(self):
        self.click_element(self.element_prev_icon())
        self.check_element_displayed(self.element_open_image())
        self.element_open_image().screenshot(self.THIRD_IMAGE_PATH)
        result = self.image_compare(self.FIRST_IMAGE_PATH, self.THIRD_IMAGE_PATH)
        assert result
