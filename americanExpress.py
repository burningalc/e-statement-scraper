from bs4 import BeautifulSoup
import requests
from credential import credential
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chromeDriver = "chromedriver.exe"
driver = webdriver.Chrome(chromeDriver)

driver.get("https://www.americanexpress.com/hk/")

username = driver.find_element_by_id("login-user")
username.click()
username.send_keys(credential['americanExpress']['username'])

password = driver.find_element_by_id("login-password")
password.click()
password.send_keys(credential['americanExpress']['password'])

driver.find_element_by_id("login-submit").click()

driver.get("https://global.americanexpress.com/myca/intl/pdfstmt/japa/statementImageInfo.do?BPIndex=0&request_type=&Face=en_HK&sorted_index=1")