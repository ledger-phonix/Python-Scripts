import httpx
from selectolax.parser import HTMLParser

import json
Data = []
def raw_data():
    resp = httpx.get('http://127.0.0.1:5500/a.html')

    html = HTMLParser(resp.text)

    scripts = html.css('script[type="text/javascript"]')
    for script in scripts:
        if 'var doc' in script.text():
            sects = script.text().split('var doc')
       
            for sect in sects:         

               
                products = {}
                keys = ['name','age', 'height', 'important', 'someDate', 'uni']
                for line in sect.splitlines():
                   
                    if line.split(':')[0].strip() in keys:
                        
                        line_data = line.split(':')
                        key = line_data[0].strip()
                        value = line_data[1].strip().replace('"', '').replace("'", '').replace(',', '')
                        products[key] = value
                    if 'onclick=tezDetay' in line:
                        line_raw = HTMLParser(line)
                        txt = line_raw.css_first('span').text()
                        products['number'] = txt
                        one = line.split('(')[1].split(')')[0].split(',')[0].replace("'", '')
                        two = line.split('(')[1].split(')')[0].split(',')[1].replace("'", '')
                        key = f'({one} | {two})'
                        products['Key'] = key    
                Data.append(products)
                    

  
raw_data()

with open('new.json', 'w', encoding='utf-8') as f:
    json.dump(Data, f , ensure_ascii= False, indent= 4)



    