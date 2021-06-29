import bs4
from requests_html import HTMLSession
from sys import version
from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
from bs4 import SoupStrainer
search_term = 'football'


main_list=[]
url =f'https://news.google.com/search?q={search_term}&hl=en-IN&gl=IN&ceid=IN%3Aen'
def get_data(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
    r = requests.get(url,headers=headers)
    soup  = BeautifulSoup(r.text,'html.parser')
    return soup
def data_parse(soup):
    var_bel  = soup.find('div',class_='FVeGwb CVnAc Haq2Hf bWfURe')
    hd = var_bel.find_all('div',class_='NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc')
# print(hd)

    for x in hd:
        news_title = x.find('a',class_='DY5T1d RZIKme').text
        news_link= x.find('a',class_='DY5T1d RZIKme')['href']
        concate = 'https://news.google.com/'+ str(news_link)
        imgs  = x.find('img',class_='tvs3Id QwxBBf')['src']

        print(news_title,imgs)
        main_dir = {
        'news_title':news_title,
        'news_link':concate,
        'news_img_links':imgs
        }
        main_list.append(main_dir)
    return

def load_data(main_list):
    df = pd.DataFrame(main_list)
    h = random.randrange(1,150)
    df.to_csv(f'main_data{h}.csv',index=False)


soup = get_data(url)
data_parse(soup)
load_data(main_list)
# for title in r.html.find('title'):
#     print(title.text)