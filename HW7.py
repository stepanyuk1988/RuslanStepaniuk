from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

print("Link(href) for header message \"California Real Estate\" is",
      driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

print("Link(src) for first home image under \"About us\" is",
      driver.find_element(By.CLASS_NAME, "wp-image-55").get_attribute("src"))

assert "California Real Estate" in driver.title
print('"California Real Estate" is in website title')
print("Website title is", driver.title)

driver.find_element(By.ID, "g2-name").click()
driver.find_element(By.ID, "g2-name").send_keys("Ruslan")
driver.find_element(By.ID, "g2-email").click()
driver.find_element(By.ID, "g2-email").send_keys("stepanyuk1988@gmail.com")
driver.find_element(By.ID, "contact-form-comment-g2-message").click()
driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys("Hi there!")
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'go back')]").click()

print("Attribute \"type\" for submit button is",
      driver.find_element(By.XPATH, "//button[@type=\"submit\"]").get_attribute("type"))

driver.close()
