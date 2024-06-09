
import requests
from bs4 import BeautifulSoup

def scrape(urls):
    DATA = []
    headers = {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    PRODUCT_URLS = urls
    for i in range(len(PRODUCT_URLS)):
        product = PRODUCT_URLS[i]
        try:
            page = requests.get(product[1],headers=headers)
        except:
            page = requests.get(product[1],headers=headers,proxies={"http": "http://111.233.225.166:1234"})
        soup = BeautifulSoup(page.content,'html.parser')
        product_name = soup.find(id='productTitle').get_text().strip()
        # to prevent script from crashing when there isn't a price for the product
        try:
            product_price = soup.find(id="priceblock_ourprice").get_text()
        except:
            product_price = soup.find("span", {"class": "a-offscreen"}).get_text()
        try:
            product_rating = soup.find("span", {"class": "a-icon-alt"}).get_text()
        except:
            product_rating = "-"
        print(product_rating)
        each_product = { "Count": i+1 , "Product" : product_name , "Price" : product_price,"Rating" : product_rating} 
        DATA.append(each_product)
    return DATA