from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)

close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
close_button.click()

sleep(2)
