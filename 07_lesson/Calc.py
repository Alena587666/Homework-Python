from CalcPage import CalcPage
from selenium import webdriver


def test_calc():
    driver = webdriver.Chrome()
    form = CalcPage(driver)

    form.set_delay(45)

    form.click_button("7")
    form.click_button("+")
    form.click_button("8")
    form.click_button("=")

    assert form.get_result() == "15"