import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

baseurl = 'https://tabelog.com/'
url = ' '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36 '
}
productlinks = []
for x in range(1, 3):
    r = requests.get(f'https://tabelog.com/aichi/C23100/rstLst/{x}/?svd=20201014&svt=1900&svps=2')

    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('h4', class_='list-rst__rst-name')


    for item in productlist:
        for link in item.find_all('a', href=True):
            print(link['href'])
            productlinks.append(url + link['href'])




resturantlist = []
for link in productlinks:
    r = requests.get(link, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')

    # try:

    name = soup.find('h2', class_='display-name').text.strip()
    rating = soup.find('b', class_='c-rating__val rdheader-rating__score-val').text.strip()

    number = soup.find('p', class_='rstinfo-table__tel-num-wrap').text.strip()

    address = soup.find('p', class_='rstinfo-table__address').text.strip()


    resturant = {

        'name': name,
        'address': address,
        'number': number,
        'ratings': rating
    }

    def write_csv(resturant, url):
        with open('restaurant_nagoya.csv', 'a' , encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)

            row = [resturant['name'], resturant['address'], resturant['number'], resturant['ratings'], url]

            writer.writerow(row)

    write_csv(resturant, link)
    # print(resturant)





