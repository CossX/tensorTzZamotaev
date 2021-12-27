import allure
from pages.yandex_image import YandexImage
from pages.yandex_search import YandexSearch


@allure.title("Поиск в яндексе")
def test_yandex_search(driver):
    with allure.step("1) Зайти на yandex.ru"):
        yandex_search = YandexSearch(driver)
        yandex_search.open_main_url()
    with allure.step("2) Проверить наличия поля поиска"):
        yandex_search.check_element_displayed(yandex_search.element_search_field())
    with allure.step("3) Ввести в поиск Тензор"):
        yandex_search.input_text_in_search_field("Тензор")
    with allure.step("4) Проверить, что появилась таблица с подсказками (suggest)"):
        yandex_search.check_suggest_is_displayed()
    with allure.step("5) При нажатии Enter появляется таблица результатов поиска"):
        yandex_search.click_enter_and_check_search_table()
    with allure.step("6) В первых 5 результатах есть ссылка на tensor.ru"):
        yandex_search.check_link_in_result("tensor.ru")

@allure.title("Картинки на яндексе")
def test_yandex_image(driver):
    with allure.step("1) Зайти на yandex.ru"):
        yandex_search = YandexSearch(driver)
        yandex_search.open_main_url()
    with allure.step("2) Ссылка «Картинки» присутствует на странице"):
        yandex_search.check_element_displayed(yandex_search.element_services_icon("Картинки"))
    with allure.step("3) Кликаем на ссылку"):
        yandex_search.click_on_services_icon("Картинки")
    with allure.step("4) Проверить, что перешли на url https://yandex.ru/images/"):
        yandex_image = YandexImage(driver)
        yandex_image.check_new_tab_url(yandex_image.YANDEX_SEARCH_IMAGES_PAGE_LINK, 2)
    with allure.step("5) Открыть 1 категорию, проверить что открылась, в поиске верный текст"):
        yandex_image.open_first_image_category_and_check()
    with allure.step("6) Открыть 1 картинку, проверить что открылась"):
        yandex_image.click_first_image_and_check()
    with allure.step("7) При нажатии кнопки вперед картинка изменяется"):
        yandex_image.click_next_and_check_image()
    with allure.step("8) При нажатии кнопки назад картинка изменяется на изображение из шага 6. Необходимо проверить, "
                     "что это то же изображение"):
        yandex_image.click_prev_and_check_image()
