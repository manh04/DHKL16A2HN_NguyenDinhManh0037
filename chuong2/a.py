import requests
import xml.etree.ElementTree as ET
import csv

# URL của RSS feed
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

# Tải nguồn cấp RSS từ URL được chỉ định và lưu dưới dạng tệp XML
response = requests.get(url)
with open('rssfeed.xml', 'wb') as file:
    file.write(response.content)

# Phân tích cú pháp tệp XML để lưu tin tức dưới dạng danh sách từ điển
tree = ET.parse('rssfeed.xml')
root = tree.getroot()

news_items = []
for item in root.findall('./channel/item'):
    news = {}
    news['title'] = item.find('title').text
    news['link'] = item.find('link').text
    news['description'] = item.find('description').text
    news_items.append(news)

# Lưu các mục tin tức vào tệp CSV
keys = news_items[0].keys()
with open('news_items.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(news_items)
import xml.etree.ElementTree as ET
import csv

# URL của RSS feed
url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

# Tải nguồn cấp RSS từ URL được chỉ định và lưu dưới dạng tệp XML
response = requests.get(url)
with open('rssfeed.xml', 'wb') as file:
    file.write(response.content)

# Phân tích cú pháp tệp XML để lưu tin tức dưới dạng danh sách từ điển
tree = ET.parse('rssfeed.xml')
root = tree.getroot()

news_items = []
for item in root.findall('./channel/item'):
    news = {}
    news['title'] = item.find('title').text
    news['link'] = item.find('link').text
    news['description'] = item.find('description').text
    news_items.append(news)

# Lưu các mục tin tức vào tệp CSV
keys = news_items[0].keys()
with open('news_items.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(news_items)