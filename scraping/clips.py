import httpx
from selectolax.parser import HTMLParser
import time
import pandas as pd
Data = []
for i in range(1, 161):
    try:
        url = f'https://motionarray.com/browse/stock-video/?page={i}'

        header = {'User-Agents':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' }
        resp = httpx.get(url, headers=header)

        html = HTMLParser(resp.text)

        nodes = html.css('div.min-w-0')
        for node in nodes:
            items = {
            'Title': node.css_first('h2.text-sm.text-white a').text(),
            'Links':'https://motionarray.com'+ node.css_first('h2.text-sm.text-white a').attributes['href'],

            }
            Data.append(items)
        print("Page:", i)
        time.sleep(6)
    except:
       pass
                   

df = pd.DataFrame(Data)
df.to_csv('Data/clips.csv', index=False)



        

