# webdriver_config.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def setup_driver():

    # Set up webdriver
    options = Options()
    options.add_argument("--start-maximized")

    # Specify the path to your webdriver
    service = Service("C:\\WebDriver\\msedgedriver.exe")

    # Initialize WebDriver
    driver = webdriver.Edge(service=service, options=options)
    
    return driver
