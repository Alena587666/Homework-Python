from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid/")

blue_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
blue_button.click()

sleep(2)
