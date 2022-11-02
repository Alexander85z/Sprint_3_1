from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def follow_personal_account(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    # ввести данные авторизации
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'trewq123@mail.ru')
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()


def test_transition_by_constructor():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    follow_personal_account(driver)

    #переход через кнопку конструктор
    driver.find_element(By.XPATH, "// p[contains(text(), 'Конструктор')]").click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "// h1[contains(text(), 'Соберите бургер')]"))).text == 'Соберите бургер'


def test_transition_by_logo_stellar():

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    follow_personal_account(driver)

    #переход через кнопку stellar burger
    driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "// h1[contains(text(), 'Соберите бургер')]"))).text == 'Соберите бургер'