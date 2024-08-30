from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_config import setup_driver

driver = setup_driver()
driver.get("https://www.dev.tokiasia.com/")
error_occurred = False
delay = 0.5  
# add category you want to test


def search(keyword):
    try:
        # Wait until the search input field is visible and clickable
        search_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div//input[@placeholder='Search ' and contains(@class, 'text-xs')]"))
        )
        # Optionally clear the existing text if any
        search_input.clear()
        
        # Send the search keyword followed by RETURN key
        search_input.send_keys(keyword + Keys.RETURN)
        
        print("Search executed successfully.")
        
    except Exception as e:
        print(f"Failed to execute search due to: {e}")
        return False
    
    return True

    



try:

    search("Inkmoth Nexus")
    time.sleep(5)

    
        
finally:
    if not error_occurred:
        print("Test succesful")
        driver.quit()

        
