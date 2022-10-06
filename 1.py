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
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('rustamgmail.com')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()

# Тест 6: Попытка регистрации с некорректно введенным телефоном
@pytest.fixture(scope="module")
def testing_exp006():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=ShYNvDk0y9I')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('rustamgmail.com')
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'))).click()
    yield
    driver.quit()

# Тест 7: Регистрация по всем правилам
@pytest.fixture(scope="module")
def testing_exp007():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=ShYNvDk0y9I')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "firstName"))).send_keys('Рустам')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "lastName"))).send_keys('Садыков')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('besonovvadim@yandex.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.name, "register"))).click()
    yield
    driver.quit()

# Тест 8: Попытка авторизации с несуществующей учетной записью
@pytest.fixture(scope="module")
def testing_exp008():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('rustam.s2012@gmail.com')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('vDDX5WBCUUK3')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "Неверный логин или пароль")))
    yield
    driver.quit()

# Тест 9: Авторизация через e-mail
@pytest.fixture(scope="module")
def testing_exp009():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys('rustam.s2012@gmail.com')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=cfd5bad0-08de-4e47-9a65-e8c0e4ee70a5&client_id=account_b2c#/')
    yield
    driver.quit()

# Тест 10: Привязка телефона к личному кабинету
@pytest.fixture(scope="module")
def testing_exp010():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "phone_action"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "rt-code"))).send_keys('******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_PHONE"))).send_keys('+7**********')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_address_submit"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.text, "rt-code"))).send_keys('******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "submit"))).click()
    yield
    driver.quit()

# Тест 11: Смена пароля через личный кабинет
@pytest.fixture(scope="module")
def testing_exp011():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_change"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=cfd5bad0-08de-4e47-9a65-e8c0e4ee70a5&client_id=account_b2c#/')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_change"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "new_password"))).send_keys('vDDX5WBCUUK3')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "confirm_password"))).send_keys('vDDX5WBCUUK3')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password_save"))).click()
    yield
    driver.quit()

# Тест 12: Авторизация через телефон
@pytest.fixture(scope="module")
def testing_exp012():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('79874407549')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys('Rustam1997')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    # driver.get('https://b2c.passport.rt.ru/account_b2c/page?state=cfd5bad0-08de-4e47-9a65-e8c0e4ee70a5&client_id=account_b2c#/')
    yield
    driver.quit()

# Тест 13: Авторизация через социальную сеть, не привязанную к личному кабинету
@pytest.fixture(scope="module")
def testing_exp013():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "oidc_google"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "view_container"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right")))
    yield
    driver.quit()

# Тест 14: Восстановление пароля при помощи e-mail
@pytest.fixture(scope="module")
def testing_exp014():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('besonovvadim@yandex.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "forgot_password"))).click()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=yO70VJtgeUI')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('besonovvadim@yandex.ru')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "captcha"))).send_keys('*******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "reset"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right"/div[1]/div[1]/div[1]/form[1]/div[1]/label[2]/span[1]/span[2]))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.label_class, "rt-btn"))).click()
    #открываем письмо со ссылкой для восстановления пароля и нажимаем кнопку "Восстановить"
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-new"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-reset-pass"))).click()
    yield
    driver.quit()

# Тест 15: Восстановление пароля при помощи телефона
@pytest.fixture(scope="module")
def testing_exp015():
    driver = webdriver.Chrome(r'B:\PyCharm\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?client_id=account_b2c&tab_id=ZmaH6_H4Jbo')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('79874407549')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "forgot_password"))).click()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys('79874407549')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "captcha"))).send_keys('*******')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "reset"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "page-right"/div[1]/div[1]/div[1]/form[1]/div[1]/label[1]/span[1]/span[3]/span[1]))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.label_class, "rt-btn"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "rt-code-0"))).send_keys('******')
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?client_id=account_b2c&tab_id=og1zRJVat3M')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-new"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys('****************')
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-reset-pass"))).click()
    yield
    driver.quit()



