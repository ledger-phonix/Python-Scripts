import requests
import json
import pandas as pd

Data = []

def scrape_data(i):
    url = 'https://www.saxo.com/dk/bestsellers/filter'
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.saxo.com/dk/bestsellere"
}
    payload = {
        'Filters': {
            'PageIndex': f'{i}'
            
            }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        
        products = data['Products']
        for product in products:
            data = {
                        'ID': product['Id'],
                        'Rank':product['Rank'],
                        'Title': product['Title'],
                        'AuthorName': product['AuthorName'],
                        'NormalPrice':product['Price']['PriceVat'], 
                        'MemberPrice': product['Price']['BenefitPriceVat'],
                        'Rating':product['Rating'],
                        'Language': product['Language']['Name'],
                        'Url': 'https://www.saxo.com/' + product['Url']
                    }
                    
            Data.append(data)
    else:
        print(f"Error: {response.status_code}")

# Run the scraping function\
        
for i in range(1,81):
    scrape_data(i)
    print('page:', i)


with open('saxo-books.json', 'w', encoding='utf-8') as f:
    json.dump(Data, f, indent= 4, ensure_ascii=False)       
      
     


df = pd.DataFrame(Data)
df.to_csv('saxo-books.csv', index=False)

print('All done')