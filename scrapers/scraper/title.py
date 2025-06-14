# scraper/runner.py
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.text
    print(f"Page title: {title}")

if __name__ == "__main__":
    scrape_page("https://www.python.org/")
