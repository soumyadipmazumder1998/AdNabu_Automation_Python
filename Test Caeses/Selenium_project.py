from Utilities.utilz import logging, take_ss, driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

#--------------------Log In--------------------#
driver.get("https://adnabu-store-assignment1.myshopify.com")
driver.maximize_window()

password = driver.find_element(By.XPATH, "//*[@id='password']")
if password.is_displayed() == True:
    logging.info("Login screen opened")
    take_ss("Login_Screen")
    print("Login screen opened")
else:
    logging.error("Login screen not opened")
    print("Login screen not opened")
password.send_keys("AdNabuQA")
driver.find_element(By.XPATH,"//*[text() = 'Enter']").click()

#-----------------------HomePage--------------------------#

if(driver.find_element(By.XPATH,"//*[contains(text(),'Shop products')]").is_displayed() == True):
    logging.info("Homepage opened")
    take_ss("Homepage")
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
    take_ss("Search Box")
    print("Search box visible")
    search_box.send_keys("Snowboard")
    search_box.send_keys(Keys.ENTER)
    if(driver.find_element(By.XPATH,"//*[text()='Search results']")).is_displayed() == True:
        logging.info("Search results opened")
        take_ss("Search Results")
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
    take_ss("Product")
    print("Product is opened")
else:
    logging.error("Product is not opened")
    print("Product is not not opened")

#------------------------Add to Cart-------------------#
add_to_cart.click()
time.sleep(4)
if(driver.find_element(By.XPATH, "//h2[contains(text(),'Your cart')]").is_displayed() == True):
    logging.info("Product added to cart")
    take_ss("Cart")
    print("Product added to cart")
else:
    logging.error("Product not added to cart")
    print("Product not added to cart")

driver.quit()