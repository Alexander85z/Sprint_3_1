from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker


def test_registration(registration):
    registration.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    registration.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()
    WebDriverWait(registration, 3)
    assert WebDriverWait(registration, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[contains(text(),'Вход')]"))).text == 'Вход'


#driver.find_element(By.XPATH, ".//h2[contains(text(),'Вход')]").text == 'Вход'