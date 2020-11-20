import requests as requests
from bs4 import BeautifulSoup
import sys
import json
# ['data']['Catalog']['searchStore']['elements']['0']['title']
#['data']['Catalog']['searchStore']['elements']['0']['description']
# ['data']['Catalog']['searchStore']['elements']['0']['effectiveDate']
# ['data']['Catalog']['searchStore']['elements']['0']['keyImages']


url='https://www.epicgames.com/store/en-US/free-games'
urlb='https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=IN&allowCountries=IN'
r = requests.get(urlb)
if(r.status_code == 200):
    jsonData = r.xml()['data']['Catalog']['searchStore']['elements']['0']['title']
    
else:
    print("Error receiving data", r.status_code)

print(jsonData)

# with open("test.txt","w", encoding="utf-8") as f:
#     print(jsonData,file=f)


