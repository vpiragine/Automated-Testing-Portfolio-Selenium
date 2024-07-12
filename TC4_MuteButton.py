from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
service = Service('')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://asoftmurmur.com/")
driver.execute_script("document.body.style.zoom='100%'")
rainSlider = driver.find_element(By.XPATH, '/html/body/div/div/div[6]/div[1]/div[1]/div/span/input')
actions = ActionChains(driver)
rainSlider_width = rainSlider.size['width']
offset = rainSlider_width * 0.75
actions.click_and_hold(rainSlider).move_by_offset(offset, 0).release().perform()
playButton = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/button[2]/div/div[1]')
playButton.click()
time.sleep(5)
muteButton = driver.find_element(By.XPATH, '/html/body/div/div/header/div/div/button')
muteButton.click()
volumeSlider = driver.find_element(By.XPATH, '/html/body/div/div/header/div/div/span/input')
volume_value = volumeSlider.get_attribute("value")
print(volume_value)
assert volume_value == "0", f"El volumen no está en cero. Valor actual: {volume_value}"
print("El volumen está en cero (muteado) correctamente.")
time.sleep(10)