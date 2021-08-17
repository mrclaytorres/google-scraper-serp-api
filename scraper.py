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

def google_result():

    # Save scraped URLs to a CSV file
    now = datetime.datetime.now().strftime('%Y%m%d-%Hh%M')
    print('Saving to a CSV file...')
    data = {"Query":used_query,"Position":ranks, "Title":page_title, "URL":urls}
    df=pd.DataFrame(data=data)
    df.index+=1
    directory = os.path.dirname(os.path.realpath(__file__))
    filename = "scrapedfile" + now + ".csv"
    file_path = os.path.join(directory,'csvfiles/', filename)
    df.to_csv(file_path)

    print('Your files are ready.')


if __name__ == '__main__':
    google_result()