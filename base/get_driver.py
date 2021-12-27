from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class GetDriver:
    def __init__(self, browser_name='Chrome'):
        if browser_name == 'Chrome':
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == 'Edge':
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())


