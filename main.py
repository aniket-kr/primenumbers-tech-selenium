import time

import pandas as pd
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from items import InfoItem

# setup selenium and chrome driver
website = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(website)

# wait for initial data fetch on first page load
driver.implicitly_wait(10)

# get the link to be clicked. We only need the first entry in the table,
# the next page buttons after that follow the order of the table.
link = driver.find_element(
    by=By.XPATH,
    value='//*[@id="table_id"]/tbody/tr[@class!="child"][1]/td[2]'
)

link.click()

# extract the first 5 items
extracted: list[InfoItem] = []
while len(extracted) < 5:
    time.sleep(1)

    closing_date = driver.find_element(
        by=By.XPATH,
        value='//td[text()="Closing Date:"]/following-sibling::td'
    ).text
    closing_iso = parse(closing_date, tzinfos={'MDT': -21600}).isoformat()

    est_value_notes = driver.find_element(
        by=By.XPATH,
        value='//td[text()="Est. Value Notes:"]/following-sibling::td'
    ).text
    est_value = list(map(
        lambda x: float(x.strip('$ ').replace(',', '')),
        est_value_notes.split('to')
    ))

    description = driver.find_element(
        by=By.XPATH,
        value='//td[text()="Description:"]/following-sibling::td'
    ).text

    extracted.append(InfoItem(description, (est_value[0], est_value[1]), closing_iso))

    next_button = driver.find_element(
        by=By.XPATH,
        value='//button[@id="id_prevnext_next"]'
    )
    next_button.click()

# close the webdriver
driver.close()
driver.quit()

# save the extracted items to csv
frame = pd.DataFrame(extracted)
frame.to_csv('output/information.csv', index=False)
frame.to_json('output/information.jsonl', orient='records', lines=True)
