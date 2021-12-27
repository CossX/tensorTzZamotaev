class Locators:
    # Общие локаторы
    YANDEX_SEARCH_FIELD = "//input[@name='text']"

    # Локаторы страницы поиска
    YANDEX_SEARCH_SUGGEST = "//div[contains(@class, 'mini-suggest__popup_visible')]"
    YANDEX_SEARCH_IMAGE_ICON = "//div[contains(text(),'{}')]"

    # Локаторы страницы результатов поиска
    YANDEX_SEARCH_RESULT_TABLE = "//ul[@id='search-result']"

    # Локаторы страницы Яндекс Картинки
    YANDEX_IMAGE_FIRST_CATEGORY = "//div[@class='PopularRequestList-Item PopularRequestList-Item_pos_0']//div[@class='PopularRequestList-SearchText']"
    YANDEX_IMAGE_FIRST_IMAGE = "//div[contains(@class, 'serp-item_pos_0')]"
    YANDEX_IMAGE_NEXT_ICON = "//div[contains(@class, 'MediaViewer_theme_fiji-ButtonNext')]"
    YANDEX_IMAGE_PREV_ICON = "//div[contains(@class, 'MediaViewer_theme_fiji-ButtonPrev')]"
    YANDEX_IMAGE_OPEN_IMAGE = "//div[@class='MMImageContainer']"
