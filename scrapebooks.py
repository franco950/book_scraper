#scraping from websites using requests
from bs4 import BeautifulSoup
import requests
htmldoc=requests.get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html')
soup=BeautifulSoup(htmldoc.text,'lxml')
#getting book titles in the category
a=[]
b=[]
for containers in soup.findAll('ol',class_='row'):
    for books in containers.findAll('a'):
        titles= (books.get('title'))
        if titles!=(None):
            titles=[titles]
            a.append(titles)
#getting prices in the category            
    for prices in soup.findAll('p',class_='price_color'):
        prices=[prices.text[1:]]
        b.append(prices)
#listing book with price        
    for a,b in zip(a,b):
      c=(a+b)
      for d in c:
          print(d)