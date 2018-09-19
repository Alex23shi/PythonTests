import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://book.douban.com/latest'
# headers
headers = {'User-Agent':"Mozilla/5.0 (X11, Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}
data = requests.get(url, headers=headers)
#print(data.text)

soup = BeautifulSoup(data.text, 'lxml')
#print(soup)

books_left = soup.find('ul', {'class':'cover-col-4 clearfix'})
books_left = books_left.find_all('li')
books_right = soup.find('ul', {'class':'cover-col-4 pl20 clearfix'})
books_right = books_right.find_all('li')
books = list(books_left)+list(books_right)
img_urls = []
titles = []
ratings = []
authors = []
details = []

for book in books:
    #img
    img_url = book.find_all('a')[0].find('img').get('src')
    img_urls.append(img_url)

    #title
    title = book.find_all('a')[1].get_text()
    titles.append(title)

    #rating
    rating = book.find('p',{'class':'rating'}).get_text()
    rating = rating.replace('\n','').replace(' ','')
    ratings.append(rating)

    #author
    author = book.find('p',{'class':'color-gray'}).get_text()
    author = author.replace('\n', '').replace(' ', '')
    authors.append(author)

    #detail
    detail = book.find_all('p')[2].get_text()
    detail = detail.replace('\n', '').replace(' ', '')
    details.append(detail)

print("img_urls: ",img_urls)
print("titles: ",titles)
print("ratings: ",ratings)
print("authors: ", authors)
print("details: ", details)

#export to csv
result = pd.DataFrame()
result['img_urls'] = img_urls
result['titles'] = titles
result['ratings'] = ratings
result['authors'] = authors
result['details'] = details
result.to_csv('result.csv', index=None)