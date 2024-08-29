from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver for your device. im using edge
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Specify the path to chromedriver
service = Service('/usr/bin/chromedriver')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# add website here
driver.get("https://www.dev.tokiasia.com/")
error_occurred = False
delay = 0.5  
# add category you want to test


def open_hamburger():
    try:
        hamburger = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "//button[@aria-expanded='false' and @aria-haspopup='dialog' and @data-state='closed' and contains(@class, 'flex')]"
            ))
        )
        hamburger.click()
        print("Opened hamburger menu")


    except Exception as e:
        print(f"Failed to open hamburger menu due to: {e}")
        return False
    return True

def open_signup_modal():
    try:
        signup = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "/html/body/div[4]/div[2]/div[1]/div/button[2]"
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
                "/html/body/div[6]/div/div[1]/a"
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
                "/html/body/div[1]/div[2]/a"
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
                "/html/body/div[1]/div[4]/div/div[2]/div/div[2]/form/div[8]/button"
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
                "/html/body/div[1]/div[4]/div/div[2]/div/div[2]/form/div[5]/button[2]"
            ))
        )
        next.click()
        print("Clicked next")


    except Exception as e:
        print(f"Failed to click nextto: {e}")
        return False
    return True


def press_login():
    try:
        login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "/html/body/div[6]/div/div[1]/form/button"
            ))
        )
        login.click()
        print("login pressed")


    except Exception as e:
        print(f"Failed to open hamburger menu due to: {e}")
        return False
    return True
    
    



try:

    open_hamburger()
    open_signup_modal()
    click_create_account()
    click_get_started()
    press_and_input_first_name("test")
    press_and_input_last_name("testlastname")
    press_and_input_display_name("testdisplay")
    press_and_input_email("testttttt@gmail.com")
    press_and_input_mobile("123456789")
    click_next()
    press_and_input_username("testUser")
    press_and_input_password("testpassword123!")
    click_submit()



    time.sleep(5)

    
        
finally:
    if not error_occurred:
        print("Test succesful")
        driver.quit()

        
