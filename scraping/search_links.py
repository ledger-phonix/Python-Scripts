from selenium import webdriver
from rich import print
import time
from selectolax.parser import HTMLParser
import csv



check_list = ['engadget', '9to5mac', 'minimalism', 'gizmodo', 'theverge', 'medium', 'techcrunch', 'thenextweb', 'wired', 'mashable', 'digitaltrends', 'techradar', 'businessinsider', 'macrumors', 'venturebeat', 'gigaom', 'slashgear', 'ubergizmo', 'blog.playstation', 'longreads', 'wealthsimple']

driver = webdriver.Chrome()
search = 'iphone security tips older mobiles'

driver.get(f'https://www.google.com/search?q={search}')



# sr.send_keys(search)
# driver(Keys.ENTER)

time.sleep(7)
for x in range(1,3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

links = []

html = HTMLParser(driver.page_source)   
nodes = html.css("div.MjjYud") 
for node in nodes:
    try:
        link = node.css_first('a').attributes['href']      
        links.append(link)
    
        
    except: 
        pass

print(len(nodes))  
 
driver.quit()
print('Total number of links:',len(links))

def filter_links(links, check_list):
    clean_links = []
    for link in links:
        found = False
        for word in check_list:
            if word in link:
                found = True
                break
        if not found and 'http' in link:
            clean_links.append(link)
    print('Total number of clean links:',len(clean_links))
    return clean_links
    

clean_links = filter_links(links, check_list)


file_name = 'Links_Data.csv'


with open(file_name, 'a', newline='') as f:
    writer = csv.writer(f)
    
    for link in clean_links:
        writer.writerow([link])

print("Links appended to", file_name)