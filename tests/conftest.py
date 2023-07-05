import pytest
from driver.driver import driver_init


def pytest_addoption(parser):
    parser.addoption(
        "--protocol",
        action="store",
        default="https",
        help="protocol: https or http")

    parser.addoption(
        "--domain",
        action="store",
        default="www.w3schools.com")

    parser.addoption(
        "--port",
        action="store",
        default=443)

    parser.addoption(
        "--browser",
        action="store",
        default='chrome')


def pytest_configure(config):
    config.protocol = config.getoption('protocol')
    config.domain = config.getoption('domain')
    config.port = config.getoption('port')
    config.browser = config.getoption('browser').upper()
    config.url = f'{config.protocol}://{config.domain}:{config.port}'
    config.url_without_port = f'{config.protocol}://{config.domain}'


@pytest.fixture(scope='function')
def driver(config, request):
    driver = driver_init(config, request.param)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def config(request):
    return request.config



