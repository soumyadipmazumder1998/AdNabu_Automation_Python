import time
from datetime import datetime
from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

#Login
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Logging
logging.basicConfig(
    filename= "C://Users//soumy//Desktop//Selenium_Python//Test Results//Logs//testlogs.txt",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO)

#Screenshots
def take_ss (step_name):
    time.sleep(1)
    timestamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = timestamp +"_"+ step_name + ".png"
    driver.save_screenshot("C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//"+filename)
