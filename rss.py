#--- imports ---#
import requests
import xml.etree.ElementTree as ET

#--- functions ---#

def load_rss():
    # create HTTP response object from given url
    # and creating and saving xml file
    url = 'https://www.prlog.org/news/us/ind/business/rss.xml'

    res = requests.get(url)

    with open('news.xml', 'wb') as f:
        f.write(res.content)


def parse_xml(xmlfile):
    # create element tree object
    # get root element
    # iterate news items

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    news_items = list()

    for item in root.findall('./channel/item'):
        news = {}

        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
            
            items.append(news)
        print(news_items)

def main():
    load_rss()
    
    news_items = parse_xml('news.xml')

if __name__ == "__main__":
    main()