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
    r = requests.get(f'https://tabelog.com/tokyo/rstLst/cond58-00-00/{x}/?LstSmoking=0&svd=20201013&svt=1900&svps=2')

    # get the first page's URL (page number 1) and identify the location of page number in URL and change the page
    # number as {x} . Because we are going to get all information from all pages using for loop.



    soup = BeautifulSoup(r.content, 'lxml')

    # use pip install lxml

    productlist = soup.find_all('h4', class_='list-rst__rst-name')
       # identify the common element cass name. Normally in website, every product is a object of one class/
       # identify that class name with its tag name.

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
        with open('restaurant.csv', 'a' , encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)

            row = [resturant['name'], resturant['address'], resturant['number'], resturant['ratings'], url]

            writer.writerow(row)

    write_csv(resturant, link)
    # print(resturant)





