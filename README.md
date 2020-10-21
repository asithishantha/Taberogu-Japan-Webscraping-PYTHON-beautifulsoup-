# Webscraping-PYTHON-beautifulsoup-tabelog 食べログ web site

For this project,Python 3.8 will be used.

For Windows installations, when installing Python make sure to check “PATH installation”. PATH installation adds executables to the default Windows Command Prompt executable search. Windows will then recognize commands like “pip” or “python” without requiring users to point it to the directory of the executable (e.g. C:/tools/python/…/python.exe). If you have already installed Python but did not mark the checkbox, just rerun the installation and select modify. On the second screen select “Add to environment variables”.

Getting to the libraries

* soup is widely used to parse the HTML files

* Pandas is used to create structured data

To install these libraries, start the terminal of your OS. Type in:

    pip install BeautifulSoup4 pandas requests lxml

_WebDrivers and browsers_

Every web scraper uses a browser as it needs to connect to the destination URL. For testing purposes i highly recommend using a regular browser.

To get started, use your preferred search engine to find the “webdriver for Chrome” (or Firefox). 

We should begin by defining our browser. Depending on the webdriver we picked back in “WebDriver and browsers” we should type in:

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36 '
    }
    

Finding a cozy place for our Python web scraper

If you already have Visual Studio Code installed, picking this IDE would be the simplest option. Otherwise, I’d highly recommend PyCharm

_Importing and using libraries_

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import csv  
    
Picking a URL

We are expecting to scrape data from many pages in targeting website.
so we have to identify the page number location, which automatically increment in the URL and use {x} for that location.
According to the below code, this script will loop 50 times to get information from 50 pages.


    
    for x in range(1, 50):
        r = requests.get(f'https://tabelog.com/chiba/rstLst/cond58-00-00/{x}/?LstSmoking=0&svd=20201014&svt=1900&svps=2')
    
        soup = BeautifulSoup(r.content, 'lxml')

    
    
_Defining objects and building lists_

Python allows coders to design objects without assigning an exact type. An object can be created by simply typing its title and assigning a value.

    # Object is “results”, brackets make the object an empty list.
    # We will be storing our data here.
    productlinks = []
    

URL, change the page number location in URL with {x} for support looping 50 times    

        productlinks = []
        for x in range(1, 50):
           
            r = requests.get(f'https://tabelog.com/chiba/rstLst/cond58-00-00/{x}/?LstSmoking=0&svd=20201014&svt=1900&svps=2')

pip install lxml

        soup = BeautifulSoup(r.content, 'lxml')
 
In Inspect(F12), identify the tag name or class name of element , which link to the inner page to get more details 
regarding each product or restaurant. save the each link to productlist.       
    
        productlist = soup.find_all('h4', class_='list-rst__rst-name')
        
    
Using for loop, get each restaurant one by one and save into productlink object

        for item in productlist:
            for link in item.find_all('a', href=True):
                print(link['href'])
                productlinks.append(url + link['href'])
                

Get each product link and direct to the inner page using requests library

    resturantlist = []
    for link in productlinks:
        r = requests.get(link, headers=headers)


get the content of the inner page using beautifulsoup

    soup = BeautifulSoup(r.content, 'lxml')
    
filter the name, rating, number and address of each restaurant's and save as variables.
find each information using their class name and the tag name

    name = soup.find('h2', class_='display-name').text.strip()
    rating = soup.find('b', class_='c-rating__val rdheader-rating__score-val').text.strip()

    number = soup.find('p', class_='rstinfo-table__tel-num-wrap').text.strip()

    address = soup.find('p', class_='rstinfo-table__address').text.strip()
    
Write into csv file 

        def write_csv(resturant, url):
        with open('restaurant_nagoya.csv', 'a', encoding='utf8') as csvfile:
            writer = csv.writer(csvfile)

            row = [resturant['name'], resturant['address'], resturant['number'], resturant['ratings'], url]

            writer.writerow(row)


    write_csv(resturant, link)
    