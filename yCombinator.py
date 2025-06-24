import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 

url = "https://www.ycombinator.com/companies"

driver = Chrome()

options = webdriver.ChromeOptions()

options.add_argument("--headless")  # Run in headless mode

options.page_load_strategy = "none"

driver = Chrome(options=options)

driver.implicitly_wait(5)

driver.get(url)
time.sleep(5)

pages = 5 
page_delay = 5 

for i in range(pages):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(page_delay)
    print(f"Page {i+1} of {pages} scrolled")

# Find all the company elements
box = driver.find_elements(By.XPATH, value="//a[@class='_company_i9oky_355']")

companies = [
    ['Title', 'Address', 'Description', 'Tags']
]

for element in box:
    title = element.find_element(By.XPATH, value=".//span[@class='_coName_i9oky_470']").text
    address = element.find_element(By.XPATH, value=".//span[@class='_coLocation_i9oky_486']").text
    description = element.find_element(By.XPATH, value=".//span[@class='_coDescription_i9oky_495']").text
    tags = element.find_element(By.XPATH, value=".//div[@class='_pillWrapper_i9oky_33']").text

    companies.append([title, address, description, tags])

driver.close()

df = pd.DataFrame(companies[1:], columns=companies[0])
df.to_csv("yCombinator.csv", index=False)
