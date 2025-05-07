print("scrape.py loaded")

#import selenium.webdriver as webdriver 
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import time 

def scrape_website(website):
    print("launching chrome browser")

    chrome_driver_path = "./chromedriver-win64/chromedriver.exe" # path to your chromedriver
    options = Options()
    driver = webdriver.Chrome(service = Service(chrome_driver_path), options = options)


    try:
        driver.get(website)
        print("page loaded .....")
        html = driver.page_source 
        time.sleep(10) 

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):

    # This function will extract the body content from the HTML
    # You can use BeautifulSoup or any other library to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.find('body')
    if body_content:
        return str(body_content)
    return ""
def clean_body_ontent(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content
def split_dom_content(dom_content, max_length=6000):
    # Split the DOM content into chunks of a specified maximum length
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)
        ]