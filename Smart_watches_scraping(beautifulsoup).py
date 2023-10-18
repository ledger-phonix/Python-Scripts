import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {
    'Title':[], 'Full_Price':[], 'Dsicount':[], 'Price':[], 'Ratings':[], 'Availability':[],'Links':[]
}

i =1 
while i <= 10:  
    #using website: priceoye.pk
   
    url = f'https://priceoye.pk/smart-watches?page={i}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')  

    links = soup.find_all('div',class_='productBox b-productBox')
    for link in links:
        final = link.find('a')
        final_links = final["href"]
        print(final_links)
        data['Links'].append(final_links)

        url = final_links
        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        title = soup.find('h3', class_='h2')
       
        data['Title'].append(title.string)
        try:
            rating= soup.find('div', class_='semi-bold rating-count')
          
            data['Ratings'].append(rating.string)

        except:
            rating = "No ratings"
            data['Ratings'].append(rating)

        try:
            full_price = soup.find('span', class_='summary-price line-through stock-info')
            data['Full_Price'].append(full_price.string)
            
        except:
            full_price= "Nill"   
            data['Full_Price'].append(full_price)  
        try:
            discount = soup.find('span',class_='save-price')
            data['Dsicount'].append(discount.string)
          
        except:
            discount= "Nill"
            data['Dsicount'].append(discount)
        try:

            price = soup.find('span', class_='summary-price text-black price-size-lg bold')
            
            data['Price'].append(price.string)
        except:
            data['Price'].append(0)


        try:
            available = soup.find('span', class_='summary-price text-black bold stock-status')
          
            data['Availability'].append(available.string)
            print(available.string)
        except:
            available = "Not Available"
            data['Availability'].append(available)
       

    i = i+1

df= pd.DataFrame.from_dict(data)
df.to_csv('All_Priceoye_watches.csv', index=False)
print("All done")