from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selectolax.parser import HTMLParser 
import pandas as pd

""""
-----------------Requirements----------------
- pip install selenium
- pip install pandas
- pip install seletolax
- Must have stable and fast internet before starting this script.

"""

data = {
    'Link':[], 'Name': [], 'Tag_line':[], 'Address':[], 'Company': []
}


username = "username "
password = "password"


driver = webdriver.Chrome()

# Navigate to LinkedIn
driver.get("https://www.linkedin.com")


username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "session_key"))
)
username_field.send_keys(username)

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "session_password"))
)
password_field.send_keys(password)


password_field.send_keys(Keys.RETURN)

time.sleep(3)

def extract_text(html,sel):
   try:
      return html.css_first(sel).text().strip()
   except AttributeError:
      return None

time.sleep(5)
# set page range here starting from 1 and ending less than 100
for x in range(1,6):

     # Enter your required linkedIn url here with required filters 
    # Must set f string link this  url bellow
    # Run the code and watch the show

    driver.get(f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22100811329%22%5D&keywords=data%20analyst&origin=FACETED_SEARCH&page={x}&sid=kGo')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)
    
    print(f'Scraping page: {x}')
    html =  HTMLParser(driver.page_source)
    nodes = html.css('li.reusable-search__result-container')
    for node in nodes:
        link = node.css_first('a').attributes['href']

        name = extract_text(node,'span[aria-hidden=true]')           
       
        tag_line = extract_text(node,'div.entity-result__primary-subtitle.t-14.t-black.t-normal')
        address = extract_text(node,'div.entity-result__secondary-subtitle.t-14.t-normal')
        position = extract_text(node, 'p.entity-result__summary.entity-result__summary--2-lines.t-12.t-black--light')
       

        
        # 'p.entity-result__summary.entity-result__summary--2-lines.t-12 t-black--light'
        data['Name'].append(name)
        data['Link'].append(link)
        data['Tag_line'].append(tag_line)
        data['Address'].append(address)

        if position is not None:
            if 'Current' in position:
                split_txt = position.split(' at ')
                comp = split_txt[-1]
                data['Company'].append(comp)
               
            else:
                data['Company'].append(None)
        else:
            data['Company'].append(None)
        
time.sleep(30)       
driver.quit()
print("File is creating............")
df= pd.DataFrame.from_dict(data)
df.to_csv('file_name3.csv', index=False)
print('File is ready to use.')


