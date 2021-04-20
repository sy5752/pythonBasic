from selenium import webdriver
import time
 
browser = webdriver.Chrome()
browser.get("http://python.org")
 
menus = browser.find_elements_by_css_selector('#top ul.menu li')