from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Config import config


def initDriver(headless):
    driver_path = Service(config.selenium_driver_path)

    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("disable-infobars");
    chrome_options.add_argument("--disable-extensions");
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=driver_path, options=chrome_options)
    return driver
