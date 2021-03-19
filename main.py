from web_scrapping import get_href_to_list
import pandas as pd

url = 'https://github.com/getmanfred/offers/wiki'
text_list, href_list = get_href_to_list(url)
element_list = []
for element in text_list:
    if ('€' or '$') and ('para' or 'en') in element:
        element_list.append(element)

print(len(element_list))




