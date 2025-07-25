from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.screenshot(path="playwright.png")
    browser.close()
    print("Screenshot saved as playwright.png")