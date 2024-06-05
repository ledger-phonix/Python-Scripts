import httpx
import json
import pandas as pd
from rich import print

def dwonload_json(url):
    resp = httpx.get(url, headers={ "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.topuniversities.com"
    } )

    for node in resp.json()['score_nodes']:
        print(node)
        yield node

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('Data/universities.csv', index= False)

def save_to_json(data):
    with open ('Data/universities.json', 'w') as f:
        json.dump(data, f, ensure_ascii= False, indent= 4)

def main():
    result = []
    for i in range(1,2):
        print("page", i)
        url = f"https://www.topuniversities.com/rankings/endpoint?nid=3897789&page={i}&items_per_page=15&tab=indicators"
        for item in dwonload_json(url):
            print(item)
            result.append(item)
    print(len(result))

    save_to_json(result)
    # save_to_csv(result)

if __name__ == '__main__':
    main()
        