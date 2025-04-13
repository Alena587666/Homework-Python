from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//span[text() = '{button_text}']")
        button.click()

    def get_result(self):
        result_element = WebDriverWait(driver,45).until(EC.text_to_be_present_in_element((By.CLASS_NAME,"result"))


