from playwright.sync_api import sync_playwright 
import time

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/")

    quotes = page.locator(".text").all_text_contents()
    authors = page.locator(".author").all_text_contents()
    

    for quote, author in zip(quotes, authors):
        print(f"{quote.strip()} - {author.strip()}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
    time.sleep(2)  # Wait for a while to see the result before closing
    print("Scraping completed.")