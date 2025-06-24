from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/" 

path = "./chromedriver-win64/chromedriver.exe" 

service = Service(executable_path=path) 
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
sub_titles = []
links = []


for container in containers:
    try:
        # Attempt to find the span element with the title
        span_element = container.find_element(by="xpath", value='./a/span')
        title = span_element.get_attribute('innerText')
        titles.append(title)
    except Exception as e:
        print("Error:", e)

    try:
        sub_title = container.find_element(by="xpath", value='./a/h3').text
        sub_titles.append(sub_title)
    except Exception as e:
        print("Error:", e)

    try:
        link = container.find_element(by="xpath", value='./a').get_attribute('href')
        links.append(link)
    except Exception as e:
        print("Error:", e)

my_dict = {'title': titles, 'sub_title': sub_titles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv', index=False)


driver.quit()
print("Data has been written to headline.csv")