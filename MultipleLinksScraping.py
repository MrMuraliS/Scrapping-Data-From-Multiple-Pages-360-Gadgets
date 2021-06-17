import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

url = 'https://gadgets.ndtv.com/mobiles/apple-phones'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')
iPhone_links = soup.select('.rvw-imgbox')

temp = pd.DataFrame()
extract_data = []
links_result = []
for i in range(len(iPhone_links)):
    links = iPhone_links[i].select('a')
    if links:
        final_link = links[0].get('href')
        links_result.append(final_link)
        # pprint.pprint(len(links_result))

        try:
            # url = 'https://gadgets.ndtv.com/apple-iphone-11-price-in-india-91110'
            req = requests.get(final_link)

            res = BeautifulSoup(req.content, 'html.parser')
            details = res.select('._st-wrp')

            table_details = details[0].select('tbody')

            for idx, item in enumerate(table_details):
                try:
                    rows_data = table_details[idx].select('tr')
                    if rows_data:
                        for idx2, item2 in enumerate(rows_data):
                            data = rows_data[idx2].select('td')
                            if data:
                                value1 = data[0].getText()
                                value2 = data[1].getText()
                                extract_data.append({value1: value2})
                except IndexError:
                    break

        except:
            print('something went wrong')

print('Process is done')

'''export_data = pd.DataFrame(extract_data)
temp.append(export_data)
temp.to_csv('iPhonesData'+'.csv')

abc = pd.read_csv('./iPhonesData.csv')
print(abc)'''
pprint.pprint(extract_data)
