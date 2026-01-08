import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://lms.threadqa.ru/xpath-practice-hub"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Find by id "#username"
def test_find_textfield_username_by_id(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "#user-name-input")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

# Find by class ".input-field"
def test_find_textfield_username_by_class(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, ".flex.h-10.w-full.border")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

# Find by attribute "input[name='email']"
def test_find_textfield_username_by_datatestid(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "input[data-testid='username-field']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

def test_find_textfield_username_by_name(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()

def test_find_textfield_username_by_placeholder(driver):
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Введите ваше имя']")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    assert element.is_displayed()