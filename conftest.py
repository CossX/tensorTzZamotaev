import allure
import pytest
from base.get_driver import GetDriver
from allure_commons.types import AttachmentType


@pytest.fixture()
def driver():
    get_driver = GetDriver()
    driver = get_driver.driver
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
