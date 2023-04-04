import os
from selenium import webdriver

import sys
sys.path.append('../linkedin_scraper')
from linkedin_scraper import actions, Person

driver = webdriver.Chrome("./driver/chromedriver")

credentials = open("credential\credentials_linkedin.txt", 'r')
creds = credentials.readlines()
email = creds[0]
password = creds[1]

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/swagatobag", driver=driver)

print(vars(person))
