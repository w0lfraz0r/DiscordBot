''' webscrap.py '''
from bs4 import BeautifulSoup
from bs4.element import Comment
import json
import requests
# ['data']['Catalog']['searchStore']['elements']['0']['title']
#['data']['Catalog']['searchStore']['elements']['0']['description']
# ['data']['Catalog']['searchStore']['elements']['0']['effectiveDate']
# ['data']['Catalog']['searchStore']['elements']['0']['keyImages']

urlsamp='https://www.epicgames.com/store/en-US/browse?q={}&sortBy=relevance&sortDir=DESC&pageSize=30'
urlb='https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=IN&allowCountries=IN'
name =""
url=""
imgurl=""

def remove_special(a_string):
    alphanumeric = ""
    for character in a_string:
        if character.isalnum():
            alphanumeric += character
    return alphanumeric


    

def find_game():
    json_data = requests.get(urlb).json()
    # print(json_data)
    d_data = json_data['data']['Catalog']['searchStore']['elements']
    # size_of_list = len(d_data)
    # for i in range(size_of_list):
    name = d_data[0]['title']
    url=urlsamp.format(remove_special(d_data[0]['title']))
    # imgurl=d_data[0]['keyImages']['url']
    return([name,url])

    
    


print(find_game())



