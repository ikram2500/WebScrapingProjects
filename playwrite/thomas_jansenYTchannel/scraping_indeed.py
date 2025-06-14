from patchright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright 
from playwright_stealth import stealth_sync

import pandas as pd
import time

def scrape_indeed(playwright):
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir = "C:\\playwright",
        channel = "chrome",
        headless = False,
        no_viewport = True,
    )
    # initiate the page
    page = browser.new_page()

    stealth_sync(page)  # make it act more human


    # keeping track of the page
    page_count = 0

    jobs = []

    #scraping the list with vacancies ()
    while page_count < 2:
        
        print ("scrapping list items")

        time.sleep(2)

        page.goto("https://pk.indeed.com/jobs?q=python+developer&start="+str(page_count * 10)+"&vjk=546532a4ea77586d")

        #getting a list of all the vacancies
        vacancies = page.locator(".cardOutline")

        for vacancy in vacancies.element_handles():

            item = {}
            item["Title"] = vacancy.query_selector("h2").inner_text()
            item['URL'] = "https://pk.indeed.com" + vacancy.query_selector("a").get_attribute("href")

            jobs.append(item)

            # incrementing the page count
        page_count += 1

    all_items = []
    # deep scraping every job
    for job in jobs:
        print("SCRAPING DETAILS PAGE")


        page.goto(job['URL'])
        time.sleep(2)
        item = {}
        item['Title'] = job['Title']
        item['URL'] = job['URL']
        item["CompanyName"] = ""
        item["Location"] = ""
        item['Salaryinfo'] = ""

        #getting the company name
        company_name = page.get_by_test_id("inLineHeader-companyName")

        if company_name.count() > 0:
            item["CompanyName"] = company_name.inner_text()

        #getting the company location
        company_location = page.get_by_test_id("inLineHeader-companyLocation")

        if company_location.count() > 0:
            item["Location"] = company_location.inner_text()

        #getting the salary info
        salary_info = page.get_by_test_id("jobsearch-OtherJobDetailsContainer")

        if salary_info.count() > 0:
            item["Salaryinfo"] = salary_info.inner_text()

        all_items.append(item)

    # closing the browser
    browser.close()
    return all_items

with sync_playwright() as playwright:
    # executing the scraping function and saving the results

    jobs = scrape_indeed(playwright)

    df=pd.DataFrame(jobs)
    df.to_csv("jobs.csv", index=False)
    print("Scraping completed. Data saved to jobs.csv")
    print(df.head())
    print("Total jobs scraped:", len(jobs))