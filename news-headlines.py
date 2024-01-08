from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
# executable will be in same folder when created 

now = datetime.now()
month_day_year = now.strftime("%d%m%Y")
# https://strftime.org/  (to set format of date and time)
website = "https://www.hindustantimes.com/"
path = "C:/Users/ankit/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe"

options = Options()
options.headless = True
service = Service(executable_path = path)

driver= webdriver.Chrome(service=service ,  options=options)
driver.get(website)

containers = driver.find_elements(by="xpath" , value='//h3[@class="hdg3"]')

titles = []
links = []
for container in containers:
    title = container.find_element(by="xpath" , value='./a').text
    titles.append(title)
    link = container.find_element(by="xpath" , value='./a').get_attribute("href")
    links.append(link)
    # (//h3[@class="hdg3"] == .)

my_dic = {'titles':titles,'links':links}
df_headlines = pd.DataFrame(my_dic)

file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()