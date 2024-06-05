import httpx
from selectolax.parser import HTMLParser
import pandas as pd

Data = []
def html_txt(url):

    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    resp = httpx.get(url, headers=headers)
    txt = resp.text
    return txt
def get_data(content):
    html = HTMLParser(content)
    nodes = html.css('div.col.span_1_of_4.church-grid')
    for node in nodes:
        name = node.css_first('p strong a').text(strip=True)
        size = node.css_first('p span a').text(strip=True)
        add = node.css_first('p span').text(strip=True)
        address = add.split('church')[-1]
        link = node.css_first('p strong a').attributes['href'] 
        data = {
            'Name':name,
            'Size': size,
            'Address': address,
            'Link':link
        }
        Data.append(data)
def make_file(Data):
    df = pd.DataFrame(Data)
    df.to_csv('Data/church.csv', index = False)
    print('File created')

def main():
    x = 0
    while x < 360:
        url =f'https://www.usachurches.org/search/searchbystate.php?start={x}&query=&denomination=&keywords=&city=&size=&statea=mi&worshipstyle='
        content = html_txt(url)
        get_data(content)
        x = x + 20
    print(len(Data))     
    make_file(Data)
main()
