import urllib.request
import os

os.makedirs('data', exist_ok=True)
url = 'https://data.ca.gov/datastore/dump/86870d5c-e9fa-46f5-8f86-2a9893662ce1'
print(f'Downloading from {url}...')
urllib.request.urlretrieve(url, 'data/grants.csv')
print('Download complete.')
