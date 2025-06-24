from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("./chromedriver-win64/chromedriver.exe"))

driver.get("https://www.flipkart.com/search?q=mobiles+under+15000+5g&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_8_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+15000+5g&requestId=334265be-7121-44a3-8c6e-060ffa37f604&as-searchtext=mobiles%20")

sleep(3)
driver.maximize_window()
sleep(2)

driver.find_element(By.ID, value=" ").send_keys("mobiles under 15000 5g")

sleep(2)

driver.find_element(By.XPATH, value="//*[@id='searchbox_homepage']/div/div/div/button").click()

sleep(2)

print("successfull")