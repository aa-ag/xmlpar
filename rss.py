#--- imports ---#
import csv
import requests
import xml.etree.ElementTree as ET

#--- functions ---#

def load_rss():
    url = 'https://www.prlog.org/news/us/ind/business/rss.xml'

    res = requests.get(url)

    with open('news.xml', 'wb') as f:
        f.write(res.content)

if __name__ == "__main__":
    load_rss()