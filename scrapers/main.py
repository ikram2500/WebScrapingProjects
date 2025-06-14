from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd

service = Service(ChromeDriverManager().install())
options = Options() 
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

try:
    url = "https://www.worldometers.info/world-population/india-population/"
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//table")))

    table = driver.find_element(By.XPATH, "//table[@class = 'datatable w-full border border-zinc-200 datatable-table']")

    headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, "th") if header.text.strip()]

    rows = []
    for row in table.find_elements(By. TAG_NAME, "tr")[1:]:
        cols = [col.text.strip() for col in row.find_elements(By.TAG_NAME, "td") ]
        if cols:
            rows.append(cols)

    df = pd.DataFrame(rows, columns=headers)
    print(df)
    df.to_csv("india_population.csv", index=False)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()