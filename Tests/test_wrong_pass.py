from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker

def test_wrong_registration(driver):
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys('12345')
    driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()

    assert driver.find_element(By.XPATH, ".//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'

