import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from faker import Faker


@pytest.fixture
def registration():
    registration = webdriver.Chrome()
    registration.get("https://stellarburgers.nomoreparties.site/")

    # открыть окно регистрации
    registration.find_element(By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]").click()
    registration.find_element(By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]").click()

    fake = Faker()
    # ввести данные регистрации
    registration.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'Дарт Вейдер')
    registration.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
         fake.email())
    registration.find_element(By.XPATH,
                        ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    registration.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]").click()

    yield registration
    registration.quit()


@pytest.fixture
def signin(driver):
# ввести данные авторизации
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'trewq123@mail.ru')
    driver.find_element(By.XPATH, ".//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    yield registration
    registration.quit()

