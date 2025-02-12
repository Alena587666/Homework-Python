from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(
service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login.")

search_field = "#username" 
driver.find_element(By.CSS_SELECTOR, search_field)
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("tomsmith")

search_field = "#password" 
driver.find_element(By.CSS_SELECTOR, search_field)
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR,
'button.fa fa-2x fa-sing-in')
login_button.click()

sleep(10)
