from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_config import setup_driver
import common_tests

driver = setup_driver()
driver.get("https://www.dev.tokiasia.com/")
error_occurred = False
delay = 0.5  
# add category you want to test



def open_login_modal():
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Log in')]"
            ))
        )
        login_button.click()
        print("Opened login modal")


    except Exception as e:
        print(f"Failed to open logindue to: {e}")
        return False
    return True

def press_and_input_username(username):
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Username']"
            ))
        )
        username_field.click()
        print("Clicked username field")
        username_field.send_keys(username)
        print("Sent keys to username field")


    except Exception as e:
        print(f"Failed to input username to: {e}")
        return False
    return True

def press_and_input_password(password):
    try:
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Password']"
            ))
        )
        password_field.click()
        print("Clicked password field")       

        password_field.send_keys(password)
        print("Sent keys to password field")


    except Exception as e:
        print(f"Failed to input password_field to: {e}")
        return False
    return True


def press_login():
    try:
        login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Log in') and @type='submit']"
            ))
        )
        login.click()
        print("login pressed")


    except Exception as e:
        print(f"Failed to open hamburger menu due to: {e}")
        return False
    return True
    
    



try:

    common_tests.open_hamburger(driver)
    open_login_modal()
    press_and_input_username("zivseller")
    press_and_input_password("TEST")
    press_login()
    time.sleep(5)

    
        
finally:
    if not error_occurred:
        print("Test succesful")
        driver.quit()

        
