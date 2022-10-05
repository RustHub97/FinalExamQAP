from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
import time
import pytest

# Тест 1: Попытка регистрации с паролем короче 8 символов
@pytest.fixture(scope="module")
def testing_exp001():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=Hg_19WEW1PQ')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('123')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('123')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Длина пароля должна быть не менее 8 символов'))).click()
    yield
    driver.quit()

# Тест 2: Попытка регистрации с несоответствующим условиям сайта именем и фамилией
@pytest.fixture(scope="module")
def testing_exp002():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=Hg_19WEW1PQ')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('Rusell123')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('Dayvox546')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'))).click()
    yield
    driver.quit()

# Тест 3: Ввести в поле "Подтверждение пароля" не тот пароль
@pytest.fixture(scope="module")
def testing_exp003():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=Hg_19WEW1PQ')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('Rustam1998')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароли не совпадают'))).click()
    yield
    driver.quit()

# Тест 4: Попытка регистрации с паролем, в котором буквы только одного регистра
@pytest.fixture(scope="module")
def testing_exp004():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=Hg_19WEW1PQ')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('rustam1997')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('rustam1997')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Пароль должен содержать хотя бы одну заглавную букву'))).click()
    yield
    driver.quit()

# Тест 5: Попытка регистрации с некорректно введенным e-mail
@pytest.fixture(scope="module")
def testing_exp005():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=Hg_19WEW1PQ')
