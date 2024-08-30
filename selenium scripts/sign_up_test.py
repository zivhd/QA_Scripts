from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_config import setup_driver
from faker import Faker
import common_tests

fake = Faker()

driver = setup_driver()
driver.get("https://www.tokiasia.com/")
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
        print(f"Failed to open signup modal due to: {e}")
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
        print(f"Failed to open create account modal due to: {e}")
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
        print("Opened get started page")
    except Exception as e:
        print(f"Failed to open get started page due to: {e}")
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
        print("Clicked first name field")
        first_name_field.send_keys(first_name)
        print("Sent keys to first name field")
    except Exception as e:
        print(f"Failed to input first name due to: {e}")
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
        print("Clicked last name field")
        last_name_field.send_keys(last_name)
        print("Sent keys to last name field")
    except Exception as e:
        print(f"Failed to input last name due to: {e}")
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
        print("Clicked display name field")
        display_name_field.send_keys(display_name)
        print("Sent keys to display name field")
    except Exception as e:
        print(f"Failed to input display name due to: {e}")
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
        print(f"Sent {email} to email field")
    except Exception as e:
        print(f"Failed to input email due to: {e}")
        return False
    return True


def digit_iterable(n):
    for digit in str(n):
        yield int(digit)

def press_and_input_mobile(mobile):
    try:
        mobile_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//input[@placeholder='+639']"
            ))
        )
        # Click the field to focus
        mobile_field.click()
        time.sleep(1)
        for key in digit_iterable(mobile):
            mobile_field.send_keys(key)
            print(f"Sent {key} to mobile field")
            time.sleep(0.1)
        time.sleep(1)  # Wait to see if the input is registered
        print(f"Sent {mobile} to mobile field")
    except Exception as e:
        print(f"Failed to input mobile due to: {e}")
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
        print(f"Sent {username} to username field")
    except Exception as e:
        print(f"Failed to input username due to: {e}")
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
        print(f"Sent {password} to confirm password field")
    except Exception as e:
        print(f"Failed to input password due to: {e}")
        return False
    return True

def click_next():
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Next')]"
            ))
        )
        next_button.click()
        print("Clicked Next")
    except Exception as e:
        print(f"Failed to click Next due to: {e}")
        return False
    return True

def click_submit():
    try:
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[contains(text(), 'Submit')]"
            ))
        )
        submit_button.click()
        print("Clicked Submit")
    except Exception as e:
        print(f"Failed to click Submit due to: {e}")
        return False
    return True


try:
    email = f"ziv.rodriguez+test{fake.random_number(digits=2, fix_len=True)}@tokiasia.com"
    common_tests.open_hamburger(driver)
    open_signup_modal()
    click_create_account()
    click_get_started()
    press_and_input_first_name(fake.name())
    time.sleep(delay)
    press_and_input_last_name(fake.last_name())
    time.sleep(delay)
    press_and_input_display_name(fake.user_name())
    time.sleep(delay)
    press_and_input_email(email)
    time.sleep(delay)
    press_and_input_mobile(fake.random_number(digits=4, fix_len=True))
    time.sleep(delay)
    click_next()
    press_and_input_username(fake.user_name())
    time.sleep(delay)
    press_and_input_password(fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True))
    time.sleep(delay) 
    click_submit()

    time.sleep(5)

finally:
    if not error_occurred:
        print("Test successful")
        
