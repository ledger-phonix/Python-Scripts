from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selectolax.parser import HTMLParser 
import pandas as pd

data = {
    'Link':[], 'Name': [], 'Tag_line':[], 'Address':[]
}
# Replace these variables with your LinkedIn credentials
username = "jamakzai12@gmail.com"
password = "Rednumber123!!!*"

# username = "talhanadeem718@gmail.com"
# password = "@Joker782"

# Path to your WebDriver (change this according to your WebDriver location)

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to LinkedIn
driver.get("https://www.linkedin.com")

# Find and fill in the username field
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "session_key"))
)
username_field.send_keys(username)

# Find and fill in the password field
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "session_password"))
)
password_field.send_keys(password)

# Submit the form (log in)
password_field.send_keys(Keys.RETURN)

# Ensure login is successful by waiting for the presence of an element on the next page
# Replace the ID below with an element that indicates successful login
# united_states= 'https://www.linkedin.com/sales/search/people?query=(spellCorrectionEnabled%3Atrue%2CrecentSearchParam%3A(id%3A2630138945%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3AINDUSTRY%2Cvalues%3AList((id%3A48%2Ctext%3AConstruction%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A320%2Ctext%3AOwner%2520%252F%2520Partner%2CselectionType%3AINCLUDED)%2C(id%3A310%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A300%2Ctext%3AVice%2520President%2CselectionType%3AINCLUDED)%2C(id%3A220%2Ctext%3ADirector%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A103644278%2Ctext%3AUnited%2520States%2CselectionType%3AINCLUDED))))%2Ckeywords%3Aroofing%2520and%2520installation)&sessionId=JNdia3cEQDyEy5vmEnnEAw%3D%3D&viewAllFilters=true'
def extract_text(html,sel):
   try:
      return html.css_first(sel).text().strip()
   except AttributeError:
      return None

time.sleep(10)
for x in range(1,41):

    driver.get(f'https://www.linkedin.com/sales/search/people?page={x}&query=(spellCorrectionEnabled%3Atrue%2CrecentSearchParam%3A(id%3A2985065594%2CdoLogHistory%3Atrue)%2Cfilters%3AList((type%3AINDUSTRY%2Cvalues%3AList((id%3A48%2Ctext%3AConstruction%2CselectionType%3AINCLUDED)))%2C(type%3ASENIORITY_LEVEL%2Cvalues%3AList((id%3A320%2Ctext%3AOwner%2520%252F%2520Partner%2CselectionType%3AINCLUDED)%2C(id%3A310%2Ctext%3ACXO%2CselectionType%3AINCLUDED)%2C(id%3A300%2Ctext%3AVice%2520President%2CselectionType%3AINCLUDED)%2C(id%3A220%2Ctext%3ADirector%2CselectionType%3AINCLUDED)))%2C(type%3AREGION%2Cvalues%3AList((id%3A102221843%2Ctext%3ANorth%2520America%2CselectionType%3AEXCLUDED))))%2Ckeywords%3Aroofing%2520and%2520installation)&sessionId=O39K2BOxQeC854lq5UCTlg%3D%3D')

    time.sleep(20)
   

    
    
    print(f'Scraping page: {x}')
    html =  HTMLParser(driver.page_source)
    nodes = html.css('li.artdeco-list__item.pl3.pv3')
    for node in nodes:
        try:
            link = "https://www.linkedin.com"+node.css_first('a').attributes['href']
        except:
            link = 'No link found'    

        name = extract_text(node,'span[data-anonymize=person-name]')           
       
        tag_line = extract_text(node,'span[data-anonymize=title]')
        address = extract_text(node,'span[data-anonymize=location]')
       

        data['Name'].append(name)
        data['Link'].append(link)
        data['Tag_line'].append(tag_line)
        data['Address'].append(address)
        print(link)
print('Creating File.........')
df= pd.DataFrame.from_dict(data)
df.to_csv('LISN-f5-1k.csv', index=False)
print('Mission Successful')



