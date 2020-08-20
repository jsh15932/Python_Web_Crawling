from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:/Users/User/Desktop/Project/0805/01 bs4/chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="search"]')

search.send_keys('black screen')
time.sleep(1)

search.send_keys(Keys.ENTER)