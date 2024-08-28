from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver for Edge
service = Service(executable_path='C:\\WebDriver\\msedgedriver.exe')
driver = webdriver.Edge(service=service)

# Open a webpage
driver.get("")
error_occurred = False
delay = 2  # Delay in seconds
category = ""

def filter_expand(filter_name):
    try:
        filter_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                f"//button[@aria-expanded='false' and contains(text(), '{filter_name}')]"
            ))
        )
        filter_box.click()
    except Exception as e:
        print(f"Failed to expand filter: {filter_name}, due to: {e}")
        return False
    return True

def ensure_filter_expanded(filter_name):
    """Ensure the filter is expanded before interacting with it."""
    try:
        filter_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH, 
                f"//button[contains(@class, 'items-center') and contains(@class, 'justify-between') and contains(@class, 'transition-all') and contains(text(), '{filter_name}')]"
            ))
        )
        # Check if filter is not expanded
        if filter_box.get_attribute('aria-expanded') == 'false':
            filter_box.click()
            print(f"Expanded filter: {filter_name}")
            time.sleep(1)  # Small delay to allow the filter to expand
    except Exception as e:
        print(f"Failed to ensure filter is expanded: {filter_name}, due to: {e}")


def click_filter_button(filter_name):
    while True:
        ensure_filter_expanded(filter_name)
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='flex']//button[@role='checkbox' and @aria-checked='false']"))
        )
        if not buttons:
            break
        button = buttons[0]
        button.click()
        print("Clicked a filter button")
        time.sleep(delay)

try:
    shop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'cursor-pointer') and contains(@class, 'font-medium') and contains(text(), 'Shop')]"))
    )
    shop_button.click()
    print("Clicked 'Shop' button")
    time.sleep(delay)
    category_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[contains(@class, 'cursor-pointer') and @href='/marketplace/{category.lower()}' and text()='{category}']"))
    )
    category_link.click()
    print(f"Clicked '{category}' category link")
    time.sleep(delay)

    click_filter_button("Fandom")

    button_locator = (By.XPATH, "//button[@type='button' and @role='checkbox' and @aria-checked='false' and @data-state='unchecked' and @value='on' and contains(@class, 'peer')]")
    while True:
            buttons = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(button_locator)
            )
            if not buttons:
                break
            button = buttons[0]
            button.click()
            print("Clicked a filter button")
            time.sleep(delay)
        

finally:
    # Close the browser only if no errors occurred
    if not error_occurred:
        driver.quit()

        
