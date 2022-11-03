from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

def input_autorization(driver):
    driver.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'trewq123@mail.ru')
    driver.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()


#вход по кнопке «Войти в аккаунт» на главной
def test_signin_in_main():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    # ввести данные авторизации
    input_autorization(driver)
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()

#вход через кнопку «Личный кабинет»
def test_signin_in_personal_account():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")
    # ввести данные авторизации
    input_autorization(driver)
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()


#вход через кнопку в форме регистрации
def test_signin_in_registration_form():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
    # ввести данные авторизации
    input_autorization(driver)
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()

#вход через кнопку в форме восстановления пароля.
def test_signin_in_pass_recovery():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
    # ввести данные авторизации
    input_autorization(driver)
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()






