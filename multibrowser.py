
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\Drivers\chrome\chromedriver.exe")
driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)
driver.close()