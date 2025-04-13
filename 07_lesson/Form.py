from FormPage import FormPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():

    driver = webdriver.Chrome()
    form = FormPage(driver)

    form.serch("Иван","Петров","Ленина,55-3","test@skypro.com","+7985899998787",
               "", "Москва", "Россия", "QA", "SkyPro")

    form.click_submit()

    assert "success" in form.check_result("first-name")
    assert "success" in form.check_result("last-name")
    assert "success" in form.check_result("address")
    assert "success" in form.check_result("e-mail")
    assert "success" in form.check_result("phone")
    assert "success" in form.check_result("zip-code")
    assert "success" in form.check_result("city")
    assert "success" in form.check_result("country")
    assert "success" in form.check_result("job-position")
    assert "success" in form.check_result("company")

    assert "danger" in driver.find_element(By.ID,"zip-code").get_attribute("class")
