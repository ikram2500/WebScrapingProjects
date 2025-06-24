#from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://www.audible.com/search"
service = Service("./chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(web)

products = driver.find_elements(By.XPATH, value="//li[contains(@class, 'productListItem')]")

book_titles = []
book_authors = []
book_length = []

for product in products:
    book_titles.append(product.find_element(By.XPATH, value=".//h3[contains(@class, 'bc-heading')]").text)
    book_authors.append(product.find_element(By.XPATH, value=".//li[contains(@class, 'authorLabel')]").text)
    book_length.append(product.find_element(By.XPATH, value=".//li[contains(@class, 'runtimeLabel')]").text)

driver.quit()

df_books = pd.DataFrame({
    "Title": book_titles,
    "Author": book_authors,
    "Length": book_length
})
df_books.to_csv("audible_books.csv", index=False)
print("Data has been written to audible_books.csv")