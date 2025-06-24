from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
import time 
from selenium.webdriver.common.by import By 
import csv 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#")

time.sleep(5)

year_elements = driver.find_elements(By.XPATH, "//a[@class='year-link']")
print(f"Number of year links found: {len(year_elements)}")

data = []

for each_year in year_elements:

    each_year.click()
    time.sleep(2)

    movie_names = driver.find_elements(By.XPATH, "//td[@class='film-title']")
    nominations = driver.find_elements(By.XPATH, "//td[@class='film-nominations']")
    film_awards = driver.find_elements(By.XPATH, "//td[@class='film-awards']")

    for each_movie, nomination_num, award_num in zip(movie_names, nominations, film_awards):
        print(f"Movie: {each_movie.text}, Nominations: {nomination_num.text}, Awards: {award_num.text}")
        data.append({
            "Movie": each_movie.text,
            "Nominations": nomination_num.text,
            "Awards": award_num.text
        })
driver.close()

# Write data to CSV
with open("movies_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Movie", "Nominations", "Awards"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)