from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
service = Service('')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://asoftmurmur.com/")
driver.execute_script("document.body.style.zoom='100%'")
moreSoundsButton = driver.find_element(By.XPATH, '/html/body/div/div/div[7]/button')


def scroll_to_element(moreSoundsButton):
    driver.execute_script("arguments[0].scrollIntoView(true);", moreSoundsButton)


scroll_to_element(moreSoundsButton)
time.sleep(3)
moreSoundsButton.click()
time.sleep(3)
streamButton = driver.find_element(By.XPATH, '/html/body/div/div/div[8]/div[2]/div/div[1]/ul/li[4]/p')
assert streamButton is not None
print('Seccion emergente es mostrada')
time.sleep(10)
