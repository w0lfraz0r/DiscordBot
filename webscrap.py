import requests
from bs4 import BeautifulSoup
from csv import writer

epic_link='https://www.epicgames.com/store/en-US/free-games'
response = requests.get(epic_link)

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='post-preview')
"""
with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(class_='post-title').get_text().replace('\n', '')
        link = post.find('a')['href']
        date = post.select('.post-date')[0].get_text()
        print("....",title,date,link)
        csv_writer.writerow([title, link, date])
"""