from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(1)

field = driver.find_element(By.TAG_NAME, "input")
field.send_keys("1000")
field.clear()
field.send_keys("999")

sleep(2)
