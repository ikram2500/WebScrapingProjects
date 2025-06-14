import asyncio 
from playwright.async_api import async_playwright  
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev/")
        await page.screenshot(path="playwright.png")
        print(await page.title())
        print(browser.version)
        print("Screenshot saved as playwright.png")
    print('test')

asyncio.run(main())