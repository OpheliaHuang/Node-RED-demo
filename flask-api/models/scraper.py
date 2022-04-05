
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import urllib.error
import time
from random import randint
import requests
from datetime import datetime
import traceback
import numpy as np
from dateutil import parser



class Scrape:
    '''This Class lets you scrape RSS feeds.
    It returns a dictionary with a unix timestamp of retrieval, as well
    as an additional python timestamp key for sorting individual articles.
    check_url_working method is included for testing'''


    def __init__(self, urls=["http://feeds.bbci.co.uk/news/technology/rss.xml"]):
        self.urls = urls

    def check_url_working(self):
        status_results = {}
        for url in self.urls:
            r = requests.get(url)
            status = r.status_code
            status_results[url] = status
        return status_results

    def news_rss(self):

        all_articles = []
        content = {}
        # content["time"] = int(time.time()) 
        for url in self.urls:
        
            try:
                r = requests.get(url)
                soup = BeautifulSoup(r.content, features='xml')
                articles = soup.findAll('item')                
                for a in articles:
                    title = a.find('title').text
                    link = a.find('link').text
                    published = a.find('pubDate').text
                    pubdate = parser.parse(published)
                    description = a.find('description').text           
                    article = {
                        'title': title,
                        'description': description,
                        'link': link,
                        'published': pubdate,
                        } 
                    all_articles.append(article)
                #content = {'time': int(time.time()) , 'articles': sorted(all_articles, key=lambda article: article['published'], reverse=True) }
            

            except Exception:
                print(traceback.print_exc())
                time.sleep(1)
            
        content = {'time': int(time.time()) , 'articles': sorted(all_articles, key=lambda article: article['published'], reverse=True) }

        return content



if __name__ == "__main__":
    result = Scrape()
    result.check_url_working()
    print(result.news_rss())

    