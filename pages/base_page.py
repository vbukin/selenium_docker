from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def visit_page(self, path=''):
        self.driver.get(f'{self.config.url}/{path}')

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))

    def click(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def fill_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def execute_script(self, code):
        self.driver.execute_script(code)
