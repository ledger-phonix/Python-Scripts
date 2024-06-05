import httpx
from bs4 import BeautifulSoup
import pandas as pd

data = {
    'Team': [], 'Player':[], 'Nationality':[], 'Details':[], 'P_Links':[]
}

url = "https://www.iplt20.com/teams"
headers={ "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.iplt20.com"
} 
resp = httpx.get(url, headers=headers)


soup = BeautifulSoup(resp.text, 'html.parser')

main_links = soup.find_all('a', class_='w-100')
for main_link in main_links:
    link1 = main_link['href']    

    url_parts = link1.split('/')

    team_name = url_parts[-1]
    print(team_name)    


    headers={ "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.iplt20.com"
    } 
    resp = httpx.get(link1, headers=headers)


    soup = BeautifulSoup(resp.text, 'html.parser')
    player_links = soup.find_all('li', class_='dys-box-color ih-pcard1')
    for p_links in player_links:
        p_link = p_links.find('a')
        single_players = p_link['href']
        data['P_Links'].append(single_players)
        data['Team'].append(team_name)

        headers={ "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "referer":"https://www.iplt20.com"
        } 
        resp = httpx.get(single_players, headers=headers)


        soup = BeautifulSoup(resp.text, 'html.parser')
        p_detail1 = soup.find('div', class_='plyr-name-nationality')
        name = p_detail1.find('h1').text
        nationality = p_detail1.find('span').text
        data['Player'].append(name)
        data['Nationality'].append(nationality)
     
       
        khali = []
        P_detail2 = soup.find_all('div', class_='grid-items')
        for p_d in P_detail2:
           hey = p_d.find('p').text
           khali.append(hey)
        
        data['Details'].append(khali)


df = pd.DataFrame.from_dict(data)
df.to_csv("IPL-Player.csv", index=False)