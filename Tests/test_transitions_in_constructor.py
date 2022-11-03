from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def go_to_login(driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
    # ввести данные авторизации
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys(
        'trewq123@mail.ru')
    driver.find_element(By.XPATH,
                        "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys(
        '123123')
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()


# тест перехода в Соусы
def test_select_souce():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    go_to_login(driver)

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Соусы')]"))).click()


    assert WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]/span"))).text == 'Соусы'

    driver.quit()


# тест перехода в Начинки
def test_select_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    go_to_login(driver)

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))).click()


    assert WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]/span"))).text == 'Начинки'
    driver.quit()


# тест перехода в Булки
def test_select_bun():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    go_to_login(driver)

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Булки')]"))).click()


    assert WebDriverWait(driver, 7).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class, 'tab_tab_type_current__2BEPc')]/span"))).text == 'Булки'
    driver.quit()
