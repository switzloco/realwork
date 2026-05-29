import requests

url = "https://bizfileonline.sos.ca.gov/api/Records/businesssearch"
payload = {
    "SEARCH_ENTITIES": {
        "FORM_DATA": {
            "SEARCH_VALUE": "Sparkz",
            "SEARCH_TYPE": "NUMBER_OR_NAME"
        }
    }
}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
try:
    r = requests.post(url, json=payload, headers=headers)
    print(r.status_code)
    print(r.text[:500])
except Exception as e:
    print("Error:", e)
