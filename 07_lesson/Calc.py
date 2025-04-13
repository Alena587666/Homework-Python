from CalcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome()
    form = CalcPage(driver)

    form.set_delay(45)

    form.click_button("7")
    form.click_button("+")
    form.click_button("8")
    form.click_button("=")
