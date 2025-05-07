import requests 
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

data = []

proceed = True

while (proceed):
    print("Processing page " + str(current_page))

    url = "https://books.toscrape.com/catalogue/page-" +str(current_page) + ".html"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    if soup.title.string == "404 Not Found":
        print("Page not found")
        proceed = False
    else:
        all_books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

        print("Page processed successfully")
        for book in all_books:
            item = {}
            item['Title'] = book.find('img').attrs['alt']
            item['link'] = book.find('a').attrs['href']
            item['Price'] = book.find('p', class_='price_color').text[1:]
            
            data.append(item)

    current_page += 1

df = pd.DataFrame(data) 
df.to_csv('books.csv', index=False)

