# import library
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# import credential
from credential import credential

# setup chromedriver
chrome = "drivers/chromedriver.exe"

# options
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("incognito")
# chromeOptions.add_argument("headless")
prefs = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": "C:\\Users\\Kenny\\Documents\\E-statement\\AE"
}
chromeOptions.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path=chrome, chrome_options=chromeOptions)

# login
driver.get("https://www.americanexpress.com/hk/")

username = driver.find_element_by_id("login-user")
username.click()
username.send_keys(credential["AmericanExpress"]["username"])

password = driver.find_element_by_id("login-password")
password.click()
password.send_keys(credential["AmericanExpress"]["password"])

driver.find_element_by_id("login-submit").click()

# get the latest pdf
driver.get("https://global.americanexpress.com/myca/intl/pdfstmt/japa/statementImageInfo.do?BPIndex=0&request_type=&Face=en_HK&sorted_index=1")


soup = BeautifulSoup(driver.page_source, "html.parser")
links = soup.find_all("a", {"class": "link"})

today = datetime.now()
for link in links:
    linkDate = datetime.strptime(link.contents[0], "%d %B %Y")
    if linkDate.year == today.year and linkDate.month == today.month - 1:
        driver.execute_script(link["href"])