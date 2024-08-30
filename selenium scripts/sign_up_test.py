
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_config import setup_driver
from faker import Faker
import common_tests

fake = Faker()

driver = setup_driver()
driver.get("https://www.dev.tokiasia.com/")
error_occurred = False
delay = 0.5  




def open_signup_modal():
    try:
        signup = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Sign Up')]"
            ))
        )
        signup.click()
        print("Opened signup modal")


    except Exception as e:
        print(f"Failed to open logindue to: {e}")
        return False
    return True

def click_create_account():

    try:
        create_account = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//a[contains(text(), 'Create an Account')]"
            ))
        )
        create_account.click()
        print("Opened create account modal")


    except Exception as e:
        print(f"Failed to open create account due to: {e}")
        return False
    return True

def click_get_started():

    try:
        get_started = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//a[contains(text(), 'Get started')]"
            ))
        )
        get_started.click()
        print("Opened create account modal")


    except Exception as e:
        print(f"Failed to open create account due to: {e}")
        return False
    return True



def press_and_input_first_name(first_name):
    try:
        first_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='First name']"
            ))
        )
        first_name_field.click()
        print("Clicked first_name field")
        first_name_field.send_keys(first_name)
        print("Sent keys to first_name field")


    except Exception as e:
        print(f"Failed to input first_name to: {e}")
        return False
    return True
def press_and_input_last_name(last_name):
    try:
        last_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Last name']"
            ))
        )
        last_name_field.click()
        print("Clicked last_name field")
        last_name_field.send_keys(last_name)
        print("Sent keys to last_name field")

    except Exception as e:
        print(f"Failed to input last_name: {e}")
        return False
    return True
def press_and_input_display_name(display_name):
    try:
        display_name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Display name']"
            ))
        )
        display_name_field.click()
        print("Clicked display_name field")
        display_name_field.send_keys(display_name)
        print("Sent keys to display_name field")

    except Exception as e:
        print(f"Failed to input display_name: {e}")
        return False
    return True
def press_and_input_email(email):
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Email']"
            ))
        )
        email_field.click()
        print("Clicked email field")
        email_field.send_keys(email)
        print("Sent keys to email field")

    except Exception as e:
        print(f"Failed to input email: {e}")
        return False
    return True
def press_and_input_mobile(mobile):
    try:
        mobile_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='+639']"
            ))
        )
        mobile_field.click()
        print("Clicked mobile field")
        mobile_field.send_keys(mobile)
        print("Sent keys to mobile field")

    except Exception as e:
        print(f"Failed to input mobile: {e}")
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
        print(f"Failed to input password_field to: {e}")
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

        confirm_password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='Confirm Password']"
            ))
        )
        confirm_password_field.click()
        print("Clicked confirm password field")       

        confirm_password_field.send_keys(password)
        print("Sent keys to confirm_password_field")


    except Exception as e:
        print(f"Failed to input password_field to: {e}")
        return False
    return True


def click_next():
    try:
        next = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Next')]"
            ))
        )
        next.click()
        print("Clicked next")


    except Exception as e:
        print(f"Failed to click nextto: {e}")
        return False
    return True

def click_submit():
    try:
        next = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Submit')]"
            ))
        )
        next.click()
        print("Clicked next")


    except Exception as e:
        print(f"Failed to click nextto: {e}")
        return False
    return True


    



try:
    
    common_tests.open_hamburger(driver)
    open_signup_modal()
    click_create_account()
    click_get_started()
    press_and_input_first_name(fake.name())
    press_and_input_last_name(fake.last_name())
    press_and_input_display_name(fake.user_name())
    press_and_input_email(fake.email())
    press_and_input_mobile(fake.random_number(digits=9, fix_len=True))
    click_next()
    press_and_input_username(fake.user_name())
    press_and_input_password(fake.password(length=8,special_chars=True,digits=True,upper_case=True,lower_case=True))
    click_submit()



    time.sleep(5)

    
        
finally:
    if not error_occurred:
        print("Test succesful")
        driver.quit()

        
