from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()


data = {'Watch Name':[], 'Watch Price':[], "Watch Ratings":[]}


driver.get("https://www.daraz.pk/watches-wsj/")



time.sleep(5)

watches = driver.find_elements(By.CLASS_NAME, 'title--wFj93')

for e in watches:
    data['Watch Name'].append(e.text)

    print(e.text)

# prices = driver.find_elements(By.CLASS_NAME, 'currency--GVKjl')

prices = driver.find_elements(By.CSS_SELECTOR, 'span.currency--GVKjl')

for p in prices:

  
    data['Watch Price'].append(p.text)
    
    print(p.text)



ratings = driver.find_elements(By.CLASS_NAME, 'rating__review--ygkUy')

for r in ratings:
    data['Watch Ratings'].append(r.text)
    print(r.text)
df = pd.DataFrame.from_dict(data)
df.to_csv('Daraz Watches.csv', index=False)


driver.quit()
