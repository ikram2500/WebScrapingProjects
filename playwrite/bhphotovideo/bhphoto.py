from playwright.sync_api import sync_playwright, Playwright
from rich import print 
import json


def run(playwright: Playwright):
    start_url = "https://www.bhphotovideo.com/c/buy/SLR-Camera-Lenses/ci/274/N/4288584247"
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(start_url)

    while True:

            for link in page.locator(
                "a[data-selenium='miniProductPageProductImgLink']"
                ).all()[:1]:
                    p = browser.new_page(base_url="https://www.bhphotovideo.com/")
                    url = link.get_attribute("href")
                    if url is not None:
                        p.goto(url)
                    else:
                        p.close()

                    data = p.locator("script[type='application/ld+json']").first.text_content()
                    json_data = json.loads(data)
                    print(json_data)
                    p.close()

            page.locator("a[data-selenium='listingPagingPageNext']").click()

        
        

with sync_playwright() as playwright:
    run(playwright)