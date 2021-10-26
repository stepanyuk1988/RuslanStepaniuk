# I am using desktop version of ZenMate VPN for working with US sites without any errors in site locators
# Highly recommend it for my Russian classmates
# It costs approx. only 300-400 rubles per month, and can be used on any machine
# Enjoy✌️
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
# from cmd > pip install Faker
from faker import Faker
fake = Faker(['ru_RU', 'en_US'])


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_send_message_chrome(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://qasvus.wordpress.com/')

        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "accept").click()
        driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Print link(href) for header message 'California Real Estate' is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Print link(src) for first home image under 'About us' is",
              driver.find_element(By.XPATH, '//*[@class = "wp-image-55"]').get_attribute("src"))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
        print("'Send Us a Message' is on the page")

        driver.find_element_by_name("g2-name").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-name").send_keys(fake.name())
        time.sleep(2)
        driver.find_element_by_id("g2-email").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_id("g2-email").send_keys(fake.email())
        time.sleep(2)
        driver.find_element_by_name("g2-message").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-message").send_keys(fake.text())
        wait = WebDriverWait(driver, 2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()

        try:
            WebDriverWait(driver, 2).\
                until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("'go back' link is visible and on the page")
        except TimeoutException:
            print("Waiting is too long")
            driver.get_screenshot_as_file("go back_link_issue.png")

        driver.find_element_by_link_text("go back").click()

        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.close()

    def test_send_message_chrome_1120x550(self):
        driver = self.driver
        driver.set_window_size(1120, 550)
        driver.get('https://qasvus.wordpress.com/')

        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "accept").click()
        # It looks strange but there is no Ad when testing with this window size second time
        # driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Print link(href) for header message 'California Real Estate' is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Print link(src) for first home image under 'About us' is",
              driver.find_element(By.XPATH, '//*[@class = "wp-image-55"]').get_attribute("src"))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
        print("'Send Us a Message' is on the page")

        driver.find_element_by_name("g2-name").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-name").send_keys(fake.name())
        time.sleep(2)
        driver.find_element_by_id("g2-email").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_id("g2-email").send_keys(fake.email())
        time.sleep(2)
        driver.find_element_by_name("g2-message").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-message").send_keys(fake.text())
        wait = WebDriverWait(driver, 2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()

        try:
            WebDriverWait(driver, 2).\
                until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("'go back' link is visible and on the page")
        except TimeoutException:
            print("Waiting is too long")
            driver.get_screenshot_as_file("go back_link_issue.png")

        driver.find_element_by_link_text("go back").click()

        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.close()

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1920, 1080)

    def test_send_message_firefox(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://qasvus.wordpress.com/')

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "accept").click()
        driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Print link(href) for header message 'California Real Estate' is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Print link(src) for first home image under 'About us' is",
              driver.find_element(By.XPATH, '//*[@class = "wp-image-55"]').get_attribute("src"))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
        print("'Send Us a Message' is on the page")

        driver.find_element_by_name("g2-name").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-name").send_keys(fake.name())
        time.sleep(2)
        driver.find_element_by_id("g2-email").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_id("g2-email").send_keys(fake.email())
        time.sleep(2)
        driver.find_element_by_name("g2-message").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-message").send_keys(fake.text())
        wait = WebDriverWait(driver, 2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()

        try:
            WebDriverWait(driver, 2).\
                until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("'go back' link is visible and on the page")
        except TimeoutException:
            print("Waiting is too long")
            driver.get_screenshot_as_file("go back_link_issue.png")

        driver.find_element_by_link_text("go back").click()

        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.close()

    def test_send_message_firefox_1250x850(self):
        driver = self.driver
        driver.set_window_size(1250, 850)
        driver.get('https://qasvus.wordpress.com/')

        time.sleep(5)
        driver.find_element(By.CLASS_NAME, "accept").click()
        driver.find_element(By.CLASS_NAME, "bottom-sticky__ad-close-btn").click()

        print("Print link(href) for header message 'California Real Estate' is",
              driver.find_element(By.XPATH, "(//a[@href='https://qasvus.wordpress.com/'])[2]").get_attribute("href"))

        print("Print link(src) for first home image under 'About us' is",
              driver.find_element(By.XPATH, '//*[@class = "wp-image-55"]').get_attribute("src"))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]")
        print("'Send Us a Message' is on the page")

        driver.find_element_by_name("g2-name").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-name").send_keys(fake.name())
        time.sleep(2)
        driver.find_element_by_id("g2-email").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_id("g2-email").send_keys(fake.email())
        time.sleep(2)
        driver.find_element_by_name("g2-message").send_keys('\n')
        time.sleep(1)
        driver.find_element_by_name("g2-message").send_keys(fake.text())
        wait = WebDriverWait(driver, 2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)
        driver.find_element_by_xpath("//button[@class='pushbutton-wide']").click()

        try:
            WebDriverWait(driver, 2).\
                until(ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            print("'go back' link is visible and on the page")
        except TimeoutException:
            print("Waiting is too long")
            driver.get_screenshot_as_file("go back_link_issue.png")

        driver.find_element_by_link_text("go back").click()

        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver.title
        print("Website title is", driver.title)

        driver.close()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
