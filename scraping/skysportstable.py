import httpx
from selectolax.parser import HTMLParser
import pandas as pd
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.skysports.com/football/tables"
}

url = "https://www.skysports.com/football/tables"

resp = httpx.get(url, headers=header)
html = HTMLParser(resp.text)

tables = html.css('table')


Data = []
for table in tables:
    table_rows = table.css('tr')

    for table_data in table_rows[1:]:  
        items = {

        'sr_no' : table_data.css_first('td.standing-table__cell').text(),
        'Team': table_data.css('td.standing-table__cell')[1].text(),
        'Pl': table_data.css('td.standing-table__cell')[2].text(),
        'GD': table_data.css('td.standing-table__cell')[3].text(),
        'Pts': table_data.css('td.standing-table__cell')[4].text()
        }
        Data.append(items)
        
            
df = pd.DataFrame(Data)
df.to_csv('table_skysports.csv', index=False)
print('All Done!')