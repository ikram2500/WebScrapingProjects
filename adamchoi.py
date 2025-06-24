import time 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By 

url = "https://www.adamchoi.co.uk/overs/detailed"

path = "/chromedriver-win64/chromedriver.exe"

driver = Chrome()

options = webdriver.ChromeOptions()
driver = Chrome(options=options)



driver.get(url)

all_matches_button = driver.find_element(By.XPATH, value="//*[@analytics-event='All matches']")
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')
print(f"Number of matches: {len(matches)}")


 
# Extract data
data = []

for match in matches:
    tds = match.find_elements(By.TAG_NAME, 'td')
    if len(tds) >= 4:
        try:
            row = {
                "date": tds[0].text.strip(),
                "home_team": tds[1].text.strip(),
                "score": tds[2].text.strip(),
                "away_team": tds[3].text.strip()
            }
            data.append(row)
            #print(row)
        except Exception as e:
            print("Error extracting row:", e)


driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("matches.csv", index=False)

print("Done. Data saved to matches.csv")

"""date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.TAG_NAME, value='td[1]').text)
    home = match.find_element(By.TAG_NAME, value='td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.TAG_NAME, value='td[3]').text)
    away_team.append(match.find_element(By.TAG_NAME, value='td[4]').text)"""