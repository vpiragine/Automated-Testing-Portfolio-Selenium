from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
service = Service('')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://asoftmurmur.com/")
driver.execute_script("document.body.style.zoom='100%'")
playStoreLink = driver.find_element(By.XPATH, '/html/body/div/div/div[5]/a[2]/span')
expected_url = playStoreLink.get_attribute("href")
playStoreLink.click()
wait = WebDriverWait(driver, 3)
current_url = "https://play.google.com/store/apps/details?id=com.gabemart.asoftmurmur"
assert current_url == "https://play.google.com/store/apps/details?id=com.gabemart.asoftmurmur"
print('URL esperada')
if len(driver.window_handles) == 1:
    print("La página se abrió en la misma ventana")
else:
    print("Se abrió una nueva ventana")
time.sleep(10)