from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\Ujjawal\Videos\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get(url="https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event = {}

for n in range(len(event_times)):
    event[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(event)
driver.close()


