import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        self.path = 'sql/trysql.asp?filename=trysql_select_all'
        super().__init__(driver, config)

    def visit(self):
        self.visit_page(self.path)

    def run_sql_click(self):
        self.find_element('.ws-btn').click()

    def get_rows(self):
        return self.find_elements('div[id="divResultSQL"] tr')

    def get_row_by_name(self, name):
        rows = self.get_rows()

        result = None
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'td')
            if cells and cells[2].text == name:
                result = row
                break

        return result

    def get_address_by_name(self, name):
        row = self.get_row_by_name(name)
        cells = row.find_elements(By.CSS_SELECTOR, 'td')
        return cells[3].text

    def fill_sql_query(self, sql_query=None):
        js_code = f'window.editor.getDoc().setValue("{sql_query}");'
        self.execute_script(js_code)

    def get_rows_count(self):
        return len(self.get_rows()) - 1

    def get_message(self):
        return self.find_element('div[id="divResultSQL"]').text

    def get_first_row(self):
        rows = self.get_rows()
        cells = rows[1].find_elements(By.CSS_SELECTOR, 'td')
        return (cell.text for cell in cells)

    def wait_until_inserted(self):
        for i in range(10):
            time.sleep(0.1)
            if self.get_message() == 'You have made changes to the database. Rows affected: 1':
                return True

        return False
