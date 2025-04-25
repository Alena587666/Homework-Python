from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def serch(self, first_name, last_name, address, e_mail, phone, zip_code, city, country, job_position, company):
       self._driver.find_element(By.NAME, "first-name").send_keys(first_name)
       self._driver.find_element(By.NAME, "last-name").send_keys(last_name)
       self._driver.find_element(By.NAME, "address").send_keys(address)
       self._driver.find_element(By.NAME, "e-mail").send_keys(e_mail)
       self._driver.find_element(By.NAME, "phone").send_keys(phone)
       self._driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
       self._driver.find_element(By.NAME, "city").send_keys(city)
       self._driver.find_element(By.NAME, "country").send_keys(country)
       self._driver.find_element(By.NAME, "job-position").send_keys(job_position)
       self._driver.find_element(By.NAME, "company").send_keys(company)

    def click_submit(self):
        self._driver.find_element(By.XPATH, '//button[text() = "Submit"]').click()

    def check_result(self, field):
        return self._driver.find_element(By.ID,field).get_attribute("class")
