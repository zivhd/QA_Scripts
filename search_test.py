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


def search(keyword):
    try:
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "/html/body/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/input"
            ))
        )
        search.click()
        print("Clicked search")
        search.send_keys(keyword)
        print(f"Entered {keyword}")

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH, 
                "/html/body/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/div[1]"
            ))
        )

        search_button.click()
        print("Clicked search button")


    except Exception as e:
        print(f"Failed to open hamburger menu due to: {e}")
        return False
    return True


    



try:

    search("Inkmoth Nexus")
    time.sleep(5)

    
        
finally:
    if not error_occurred:
        print("Test succesful")
        driver.quit()

        
