import requests
url = 'https://file.lacounty.gov/SDSInter/ceo/asp/1201807_PATHCares-IH-May2025.pdf'
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(r.status_code)
print(len(r.content))
