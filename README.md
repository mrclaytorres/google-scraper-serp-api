# Google Scraper Serp API
## google-scraper-serp-api

### Install Dependencies
```
$ pip install -r requirements.txt
```

### Create Your Credentials
* 1. Assuming you already registered to SERP API (serpapi.com) and have your API key.
* 2. Create a *creds.py* file in your project's root directory
        * Inside your *creds.py*, create your credentials like this:
            ``` 
            apikey = "YOUR API KEY HERE"
            ``` 

### Create Input File

* 1. Use the search_query_sample.csv and renamed it search_query.csv
* 2. Inside the search_query.csv are the two input parameters
        * query - The search query you input in Google's search field.
        * location - The location from where the request is coming from.

### Running The Script
```
$ python scraper.py
```

### Output
* The output should be inside the *csvfiles/* folder

### Other Resources
* [https://serpapi.com/search-api](https://serpapi.com/search-api)