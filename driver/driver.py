from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.constans.enums import Browser


def driver_init(config, screen_size):
    if config.browser == Browser.CHROME.value:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument(f'--window-size={screen_size.value[0]},{screen_size.value[1]}')
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    else:
        raise ValueError(f"Invalid browser: {config.browser}")

    return driver
