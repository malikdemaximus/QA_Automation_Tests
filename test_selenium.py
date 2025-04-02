from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()
