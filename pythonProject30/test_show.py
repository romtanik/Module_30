import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show_all_pets(driver):
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('romt@gmail.com')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('asd123')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


def test_show_my_pets(web_driver):
    time.sleep(3)
    # Вводим email
    web_driver.find_element(By.ID, 'email').send_keys('romt@gmail.com')
    # Вводим пароль
    web_driver.find_element(By.ID, 'pass').send_keys('asd123')
    # Нажимаем на кнопку входа в аккаунт
    web_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert web_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    images = web_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = web_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = web_driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')



    for i in range(len(names)):
        image_source = images[i].get_attribute('src')
        name_text = names[i].text
        print(f"Image source: {image_source}")
        print(f"Name text: {name_text}")
        assert image_source != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_show_my_pets(driver):

    driver.find_element(By.ID, 'email').send_keys('romt@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('asd123')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')

    assert int(pets_number) == len(pets_count)
