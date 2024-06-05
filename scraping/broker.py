import httpx
from selectolax.parser import HTMLParser
import pandas as pd
Data = []
def get_text(url):
    headers = {'User-Agents':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    resp = httpx.get(url, headers=headers, follow_redirects=True)
    
    return resp.text
def get_links(html_txt):
    html = HTMLParser(html_txt)
    nodes = html.css('div.part-pan')
    for node in nodes:
        url = node.css_first('a').attributes['href']
        page_txt = get_text(url)
        page_data(page_txt)
def page_data(page_html):
    html = HTMLParser(page_html)
    table_rows = html.css('table tbody tr')
    table_dict = {}
    for row in table_rows:
        Keys = row.css('td')
        table_dict[Keys[0].text(strip=True)] = Keys[1].text(strip=True)
    Data.append(table_dict)    
def make_file(Data):
    df = pd.DataFrame(Data)
    df.to_csv('Data/broker.csv', index=False)
def main(): 
    for x in range(1, 67):
        print('Page:', x)           
        url = f'https://brokersireland.ie/broker/page/{x}/'
        html_txt = get_text(url)
        get_links(html_txt)
    make_file(Data)    
if __name__ == '__main__':
    main()
