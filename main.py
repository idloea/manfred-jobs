from bs4 import NavigableString

from extract_from_string import extract_number_list_from_spaced_string
from web_scrapping import get_href_to_list
import pandas as pd

url = 'https://github.com/getmanfred/offers/wiki'
text_list, href_list = get_href_to_list(url)

job_list = []
for element in text_list:
    if isinstance(element, NavigableString) and '(' in element:
        job_list.append(element)

df = pd.DataFrame(job_list, columns=['ManfredName'])

df['Salary'] = df.apply(lambda row: extract_number_list_from_spaced_string(row['ManfredName']), axis=1)




