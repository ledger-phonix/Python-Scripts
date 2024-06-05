import httpx
from selectolax.parser import HTMLParser
url = 'https://corp.delaware.gov/agents/'
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}

resp = httpx.get(url, headers=header)


html = HTMLParser(resp.text)
nodes = html.css('div.modal')

for node in nodes:
    # txt = node.css_first('div.modal-body p:contains("Phone:")').text(strip=True).split(":")[1]
    txt = node.css('div.modal-body p')
    print(txt[2].text(strip=True).split(':')[1])
    
