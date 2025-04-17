from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID,"shopping_cart_container").click()
    driver.find_element(By.ID,"checkout").click()
    driver.find_element(By.ID,"first-name").send_keys("Evgen")
    driver.find_element(By.ID,"last-name").send_keys("LN")
    driver.find_element(By.ID,"postal-code").send_keys("601500")
    driver.find_element(By.ID,"continue").click()
    total_price = driver.find_element(By.CLASS_NAME,'summary_total_label')
    total = total_price.text.strip().replace("Total: $","")

    expected_total = "58.29"
    assert total == expected_total
