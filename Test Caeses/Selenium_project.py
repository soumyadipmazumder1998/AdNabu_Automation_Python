from time import thread_time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

#Logging
logging.basicConfig(
    filename= "C://Users//soumy//Desktop//Selenium_Python//Test Results//Logs//testlogs.txt",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#--------------------Log In--------------------#
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://adnabu-store-assignment1.myshopify.com")
driver.maximize_window()

password = driver.find_element(By.XPATH, '//*[@id="password"]')
WebDriverWait(driver, 10)
if password.is_displayed() == True:
    logging.info("Login screen opened")
    driver.save_screenshot(filename="C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//1_Login.png")
    print("Login screen opened")
else:
    logging.error("Login screen not opened")
    print("Login screen not opened")
password.send_keys("AdNabuQA")
driver.find_element(By.XPATH,"//*[text() = 'Enter']").click()

#-----------------------HomePage--------------------------#

if(driver.find_element(By.XPATH,"//*[contains(text(),'Shop products')]").is_displayed() == True):
    logging.info("Homepage opened")
    driver.save_screenshot(filename = "C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//2_Homepage.png")
    print("Homepage opened")
else:
    logging.error("Homepage not opened")
    print("Homepage not opened")

#---------------Search box and Search Result page validation----------------#

driver.find_element(By.XPATH,"(//*[contains(@class,'icon-search')])/parent::span").click()
WebDriverWait(driver, 10)
search_box = driver.find_element(By.XPATH, "(//*[contains(text(),'Search')])/preceding-sibling::input")
if(search_box.is_displayed() == True):
    logging.info("Search box visible")
    driver.save_screenshot(filename="C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//3_Search box.png")
    print("Search box visible")
    search_box.send_keys("Snowboard")
    search_box.send_keys(Keys.ENTER)
    if(driver.find_element(By.XPATH,"//*[text()='Search results']")).is_displayed() == True:
        logging.info("Search results opened")
        driver.save_screenshot(filename = "C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//4_Search Results.png")
        print("Search results opened")
    else:
        logging.error("Search results not opened")
        print("Search results not opened")
else:
    logging.error("Search box not visible")
    print("Search box not visible")

#-------------------------Product page-------------------------#
WebDriverWait(driver, 10)
driver.find_element(By.XPATH,"(//a[contains(text(),'The Complete Snowboard')])[2]").click()
add_to_cart= driver.find_element(By.XPATH, "//span[contains(text(),'Add to cart')]/parent::button")
if(add_to_cart.is_displayed() == True):
    logging.info("Product is opened")
    driver.save_screenshot(filename = "C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//5_Product.png")
    print("Product is opened")
else:
    logging.error("Product is not opened")
    print("Product is not not opened")

#------------------------Add to Cart-------------------#
add_to_cart.click()
time.sleep(5)
if(driver.find_element(By.XPATH, "//h2[contains(text(),'Your cart')]").is_displayed() == True):
    logging.info("Product added to cart")
    driver.save_screenshot(
    filename="C://Users//soumy//Desktop//Selenium_Python//Test Results//Screenprints//6_Cart.png")
    print("Product added to cart")
else:
    logging.error("Product not added to cart")
    print("Product not added to cart")

driver.quit()




