import requests
from selectolax.parser import HTMLParser


url = 'https://www.bezorgdekrant.nl/en/all-jobs'
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.bezorgdekrant.nl/en/all-jobs"
}

resp = requests.get(url, headers=headers)

print(resp.status_code)

html = HTMLParser(resp.text)
hi = []


nodes = html.css('a.vacancy-card.icon-chevron-right')
# print(nodes)
for node in nodes:
    name = node.css_first('h4').text(separator='', strip=True)
    # print(name)
    if ' in ' in name:
        city = name.split(' in ')
        city1 = city[-1].strip().lower().title()
        hi.append(city1)
    else:
        city = name.split(' IN ') 
        city1 = city[-1].strip().lower().title()
        hi.append(city1)

for cities in hi:
    print(cities)

print(len(hi))