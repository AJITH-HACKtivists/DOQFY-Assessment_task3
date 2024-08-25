import requests
from bs4 import BeautifulSoup
import json
from redis import Redis
redis_conn = Redis()
def scrape_data():
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://www.nseindia.com/market-data/live-equity-market'
    }
    initial_url = 'https://www.nseindia.com'
    session.get(initial_url, headers=headers)
    url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050'
    response = requests.get(url, headers=headers, cookies=session.cookies.get_dict())
    if response.status_code == 200:
        data = response.json()  # Parse JSON response

        # Extract relevant information from the JSON data
        nifty_data = data.get('data', [])  # Assuming the relevant data is under 'data' key
        redis_conn.set('nifty_50', json.dumps(nifty_data))

        print("Scraped and stored Nifty 50 data successfully")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")