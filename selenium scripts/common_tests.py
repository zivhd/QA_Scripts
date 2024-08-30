from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_hamburger(driver):
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
