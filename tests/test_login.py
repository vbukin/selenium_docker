import pytest
from utils.constans.enums import ScreenSize
from pages.login_page import LoginPage


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_check_address_by_name(driver, config):
    login_page = LoginPage(driver, config)
    login_page.visit()
    login_page.run_sql_click()
    address = login_page.get_address_by_name('Giovanni Rovelli')
    assert address == 'Via Ludovico il Moro 22'


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_check_city_london_count(driver, config):
    login_page = LoginPage(driver, config)
    login_page.visit()
    sql_query = "SELECT * FROM Customers where city='London';"
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()
    assert login_page.get_rows_count() == 6


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_add_new_row(driver, config):
    login_page = LoginPage(driver, config)
    login_page.visit()

    person = ('Company A', 'John Doe', '123 Main St', 'New York', '10001', 'USA')
    sql_query = f"INSERT INTO customers (CustomerName, ContactName, Address, City, PostalCode, Country) VALUES ( '{person[0]}', '{person[1]}', '{person[2]}', '{person[3]}', '{person[4]}', '{person[5]}');"
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    assert login_page.wait_until_inserted() is True

    sql_query = 'SELECT * FROM customers  WHERE CustomerID = (SELECT MAX(CustomerID) FROM customers);'
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    _, *new_person = login_page.get_first_row()
    assert tuple(new_person) == person


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_update_row(driver, config):
    login_page = LoginPage(driver, config)
    login_page.visit()

    person = ('New Company A', 'New John Doe', 'New Main St', 'New New York', 'New 10001', 'New USA')
    sql_query = f"UPDATE customers SET CustomerName = '{person[0]}', ContactName = '{person[1]}', Address = '{person[2]}', City = '{person[3]}', PostalCode = '{person[4]}', Country = '{person[5]}' WHERE CustomerID = 1;"
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    assert login_page.wait_until_inserted() is True

    sql_query = 'SELECT * FROM customers  WHERE CustomerID = 1;'
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    _, *new_person = login_page.get_first_row()
    assert tuple(new_person) == person


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_delete_row(driver, config):
    login_page = LoginPage(driver, config)
    login_page.visit()

    sql_query = 'DELETE FROM customers WHERE CustomerID = 1;'
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    assert login_page.wait_until_inserted() is True

    sql_query = 'SELECT * FROM customers  WHERE CustomerID = 1;'
    login_page.fill_sql_query(sql_query)
    login_page.run_sql_click()

    assert login_page.get_message() == 'No result.'
