import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://lms.threadqa.ru/xpath-practice-hub"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# "[@id='id name']"                 # по id
def test_find_textfield_username_by_id(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//input[@id='user-name-input']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

# "//input[@name='username']"       # по атрибуту
def test_find_textfield_username_by_name(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//input[@name='username']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

def test_find_textfield_username_by_placeholder(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//input[@placeholder='Введите ваше имя']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

def test_find_textfield_username_by_datatestid(driver):
    driver.get(url)
    element = driver.find_element(By.XPATH, "//input[@data-testid='username-field']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()


