from FormPage import FormPage
from selenium import webdriver


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
    assert "success" in form.check_result("city")
    assert "success" in form.check_result("country")
    assert "success" in form.check_result("job-position")
    assert "success" in form.check_result("company")

    assert "danger" in form.check_result("zip-code")
