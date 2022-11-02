from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest


def test_signin_in_main():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    # ввести данные авторизации
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'trewq123@mail.ru')
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()


def test_signin_in_main1(signin):

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    assert WebDriverWait(signin, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".// button[contains(text(), 'Оформить заказ')]"))).text == 'Оформить заказ'

    driver.quit()



