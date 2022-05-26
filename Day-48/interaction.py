from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\Ujjawal\Videos\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
count.click()

