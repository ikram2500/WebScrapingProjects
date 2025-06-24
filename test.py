from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 


website = "https://www.thesun.co.uk/sport/football/" 

path = "./chromedriver-win64/chromedriver.exe" 

service = Service(executable_path=path) 

options = Options()
options.add_argument("--headless")  # Optional: run in background
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")

driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
print("Number of containers found:", len(containers))
for container in containers:
    try:
        """span_element = container.find_element(by="xpath", value='./a/span')
        title = span_element.get_attribute('innerText')
        sub_title = container.find_element(by="xpath", value='./a/h3').text
        #sub_titles.append(sub_title)
        print("Sub-title:", sub_title)
        print("Title:", title)"""
        link = container.find_element(by="xpath", value='./a').get_attribute('href')
        print("Link:", link)
    except Exception as e:
        print("Error:", e)