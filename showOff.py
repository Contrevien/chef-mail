import os
from selenium import webdriver

chromedriver = "/Users/User/Downloads/Compressed/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.codechef.com/problems/CLKLZM")
driver.quit()
