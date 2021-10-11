from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import datetime
import sys
import os
import os.path
import time
import csv
from serpapi import GoogleSearch
import creds

def google_result():

    ranks = []
    page_title = []
    urls = []
    used_query = []
    search_query_list = []
    time_start = datetime.datetime.now().replace(microsecond=0)

    #Get search query and concatinate it to the url summary
    with open('search_query.txt', 'r', encoding='UTF8') as search_queries:
        for query in search_queries:
            search_query_list.append(query)

    for query in search_query_list:
        print(f'Searching for query: {query}')
        params = {
            "engine": "google",
            "q": query,
            "gl": "us",
            "num": "200",
            "api_key": creds.apikey
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        
        try:
            if results['organic_results']:

                organic_results = results['organic_results']
                
                for item in organic_results:
                    ranks.append(item['position'])
                    page_title.append(item['title'])
                    urls.append(item['link'])
                    used_query.append(results['search_parameters']['q'])
            else:
                pass
        except:
            pass
    
    time_end = datetime.datetime.now().replace(microsecond=0)
    runtime = time_end - time_start
    print(f"Script runtime: {runtime}.")

    # Save scraped URLs to a CSV file
    now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
    print('Saving to a CSV file...')
    data = {"Query":used_query,"Position":ranks, "Title":page_title, "URL":urls}
    df=pd.DataFrame(data=data)
    df.index+=1
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "SerpAPIscrapedfile" + now + ".csv"
    file_path = os.path.join(directory,'csvfiles/', filename)
    df.to_csv(file_path)

    print('Your files are ready.')


if __name__ == '__main__':
    google_result()