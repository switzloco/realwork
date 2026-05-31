import requests
url = 'https://USY9HV4C4P-dsn.algolia.net/1/indexes'
headers = {'X-Algolia-Application-Id': 'USY9HV4C4P', 'X-Algolia-API-Key': 'a66f1d6fe5ef613ce81b6cf0138b4c16'}
try:
    print(requests.get(url, headers=headers).json())
except Exception as e:
    print(e)
