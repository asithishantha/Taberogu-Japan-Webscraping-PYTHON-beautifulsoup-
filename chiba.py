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
# productlink object
productlinks = []
for x in range(1, 50):
    # URL, change the page number location in URL with {x} for support looping 50 times
    r = requests.get(f'https://tabelog.com/chiba/rstLst/cond58-00-00/{x}/?LstSmoking=0&svd=20201014&svt=1900&svps=2')

    soup = BeautifulSoup(r.content, 'lxml')
    # pip install lxml

    productlist = soup.find_all('h4', class_='list-rst__rst-name')
    # in Inspect(F12), identify the tag name or class name of element , which link to the inner page to get more details
    # regarding each product or restaurant. save the each link to productlink object.

    # using for loop get each restaurant one by one
    for item in productlist:
        for link in item.find_all('a', href=True):
            print(link['href'])
            productlinks.append(url + link['href'])
            # save into productlink object

resturantlist = []
for link in productlinks:
    r = requests.get(link, headers=headers)
    # get each product link and redirect to the inner page using requests library

    soup = BeautifulSoup(r.content, 'lxml')
    # get the content of the inner page using beautifulsoup

    # try:

    # filter the name, rating, number and address of each restaurant's and save as variables.
    # find each information using their class name and the tag name

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
        with open('restaurant_nagoya.csv', 'a', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)

            row = [resturant['name'], resturant['address'], resturant['number'], resturant['ratings'], url]

            writer.writerow(row)


    write_csv(resturant, link)
    # print(resturant)
