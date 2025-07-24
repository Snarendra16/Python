# Web scrapping 

'''
Urls
1. https://python.langchain.com/docs/introduction/
2. https://python.langchain.com/docs/tutorials/
3. https://python.langchain.com/docs/concepts/

'''

import threading
from bs4 import BeautifulSoup
import requests

url=['https://python.langchain.com/docs/introduction/',
     'https://python.langchain.com/docs/tutorials/',
     'https://python.langchain.com/docs/concepts/']

def fetch_content(url):
    responce=requests.get(url)
    soup=BeautifulSoup(responce.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads=[]

for url in url:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"All webpages are fetched from URLs")

t1=threading.Thread(target=url)