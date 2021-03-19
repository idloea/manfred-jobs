from bs4 import NavigableString
from web_scrapping import get_href_to_list
import pandas as pd

url = 'https://github.com/getmanfred/offers/wiki'
text_list, href_list = get_href_to_list(url)

job_list = []
for element in text_list:
    if isinstance(element, NavigableString) and '(' in element:
        job_list.append(element)

df = pd.DataFrame(job_list, columns=['ManfredName'])

df['Split'] = df['ManfredName'].str.split('(', 1)
df['Job'] = df['Split'].str[0]
df['Split2'] = df['Split'].str[1].str.split(')', 1)
df['Salary'] = df['Split2'].str[0]
df['RestInfo'] = df['Split2'].str[1]
