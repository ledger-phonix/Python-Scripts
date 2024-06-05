import requests
import json
import pandas as pd
import time
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.shopify.com/partners/directory/services"}

def able(script):
    try:
        site = script
        return site
        
    except AttributeError:
        return None

def make_links():
    Data = []
 
    for i in range(1, 81):
        print('Scrpaing page: ', i)
        url = f'https://www.shopify.com/partners/directory/services?page={i}&_data=pages%2F%28%24locale%29%2Fpartners%2Fdirectory%2Fservices'
        time.sleep(3)
        resp = requests.get(url,headers=headers, timeout=10)

        profiles = resp.json()['profiles']        
        for profile in profiles:
            partner = profile['handle']
            full_link = (f'https://www.shopify.com/partners/directory/partner/{partner}?_data=pages%2F%28%24locale%29%2Fpartners%2Fdirectory%2Fpartner%2F%24partner')
            main_link = full_link.split('?')
            time.sleep(2)
            resp_2 = requests.get(full_link,headers=headers, timeout=10)

            links_data = resp_2.json()
            print('Scaping page details...')
            items = {
                'BusinessName': profile['businessName'],
                'Location' : profile['location'],
                'Languages' : profile['languages'],
                'Ratings': profile['ratings']['avg'],
                'Reviews': profile['ratings']['total'],
                'SartingPrice': profile['pricingInfo']['startingPrice'],
                'Website': able(links_data['profile']['websiteUrl']),
                'ContactEmail': links_data['profile']['contactEmail'],
                'ContactPhoneNumber': links_data['profile']['contactPhoneNumber'],
                'ServiceURL': main_link[0]
            }
            print(items)
            Data.append(items)
  

    return Data

data = make_links()
print('creating Files')

df = pd.DataFrame(data)
df.to_csv('shopify_services.csv', index=False)

with open('shopify_services.json', 'w') as f:
    json.dump(data, f, indent= 4)



