from playwright.sync_api import sync_playwright

import time
playwright = sync_playwright().start() 
browser = playwright.chromium.launch_persistent_context(
        user_data_dir = "C:\\playwright",
        channel = "chrome",
        headless = False,
        no_viewport = True,
    )
page = browser.new_page()

print ("scrapping list items")

time.sleep(2)

page.goto("https://arxiv.org/search/cs")
page.get_by_placeholder("search term").fill('neural networks')
page.get_by_role("button", name="Search").nth(1).click()
time.sleep(2)
browser.close()

