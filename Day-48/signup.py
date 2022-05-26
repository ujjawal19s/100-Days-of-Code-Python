from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Ujjawal\Videos\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.CSS_SELECTOR, ".top")
first_name.send_keys("Ujjawal")

last_name = driver.find_element(By.CSS_SELECTOR, ".middle")
last_name.send_keys("Singh")

email_text = driver.find_element(By.CSS_SELECTOR, ".bottom")
email_text.send_keys("singhujjawal660@gmail.com")

btn = driver.find_element(By.CSS_SELECTOR, ".btn")
btn.send_keys(Keys.ENTER)
