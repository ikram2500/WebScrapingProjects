from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import pandas as pd

website = "https://www.bhphotovideo.com/c/buy/SLR-Camera-Lenses/ci/274/N/4288584247" 

path = "./chromedriver-win64/chromedriver.exe" 

service = Service(executable_path=path) 
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//h3[@data-selenium="miniProductPageName"]//span[@data-selenium="miniProductPageProductName"]')
print([container.text for container in containers])