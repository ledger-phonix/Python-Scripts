import httpx
import json
import pandas as pd
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://dtm.com/en/results"}

url = 'https://api.dtm.com/data?query=drivers&lang=en'


def save_to_json(data):
    with open('Data/dtm.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii= False, indent= 4)
def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('Data/dtm.csv', index= False)

def get_data(url, headers):
    resp = httpx.get(url, headers=headers)
    for node in resp.json()['drivers']:
        yield node

def main():
    data = []
    for drivers in get_data(url,headers):
        data.append(drivers)

    print(len(data))

    # for entry in data:
    #     try:
    #         first_name = entry.get("firstName")
    #         last_name = entry.get('lastName')
    #         facebook_url = entry.get("appDriverSocialMedia", {}).get("facebookUrl")
    #         country = entry.get("country", {}).get("name")
    #         print(first_name, last_name)
    #         print(facebook_url, '\n',country)
    #     except:
    #         pass


    # save_to_json(data)
    # save_to_csv(data)
if __name__ == '__main__':
    main()


print('worked successfully')
