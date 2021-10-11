# Google Scraper Serp API
## google-scraper-serp-api

### Install Dependencies
```
$ pip install -r requirements.txt
```

### Create Your Credentials
* Assuming you already registered to SERP API (serpapi.com) and have your API key.
* Create a **creds.py** file in your project's root directory
        * Inside your **creds.py**, create your credentials like this:
            ``` 
            apikey = "YOUR API KEY HERE"
            ``` 

### Create Input File
* Use the search_query_sample.csv and renamed it search_query.csv
* Inside the search_query.csv are the two input parameters
    * query - The search query you input in Google's search field.
    * location - The location from where the request is coming from.

### Create Output Folder
* On your project's root directory, create a folder named **csvfiles**.
* The output should be inside the **csvfiles** folder

### Running The Script
```
$ python scraper.py
```

### Other Notes
* If you wanted to include SERP Pagination results (>10), just add `num` in the `params` object, up to 10th page.
    ```
    params = {
                "engine": "google",
                "q": query,
                "num": 200,
                "location": location,
                "gl": "us",
                "api_key": creds.apikey
            }
    ```

### Other Resources
* [https://serpapi.com/search-api](https://serpapi.com/search-api)