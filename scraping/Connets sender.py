from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selectolax.parser import HTMLParser
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'
    
links= []

names =[]


#<-------------editing section -------------->
username = "talhanadeem718@gmail.com"
password = "#LItalha@782"



msg = '''I hope this message finds you well. I'm Talha, passionate about web scraping using Python and diving into data analysis with PowerBI, Tableau, and SQL. I'd love to connect and share insights in our shared field. Looking forward to the possibility of connecting!

Best regards,
Talha '''

#<-------------editing section -------------->


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

time.sleep(5)
# set page range here starting from 1 and ending less than 100
for x in range(1,2):

    # Enter your required linkedIn url here with required filters 
    # Must set f string link this  url bellow
    # Run the code and watch the show
    
    driver.get(f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22101174742%22%2C%22103644278%22%5D&keywords=python%20automation%20data%20analysis%20 python&origin=FACETED_SEARCH&page={x}&sid=YRh')
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    
    print(f'Collecting Profile links from page: {x}')
    html =  HTMLParser(driver.page_source)
    nodes = html.css('li.reusable-search__result-container')
    for node in nodes:
        link = node.css_first('a').attributes['href']
        links.append(link)
        try:
            name = node.css_first('span[aria-hidden=true]').text().strip()
            names.append(name)
        except:
            names.append('Dear')

print(f'Total profile links collected: {len(links)} \nGoing to each link for sending connections')
time.sleep(3)
for link , name, i in zip(links, names, range(1,len(links)+1)):
    driver.get(link)
 
    print(f"Sending connection to {Color.GREEN}{name}{Color.END}[{Color.RED}{i}{Color.END}]\n")

    time.sleep(5)
    try:
        cnt_btn = driver.find_elements(By.TAG_NAME, 'button')
        for btn in cnt_btn:
            if btn.text == 'Connect':
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
                try:
                    add_note = driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
                    driver.execute_script("arguments[0].click();", add_note)
                    time.sleep(3)

                    text = driver.find_element(By.TAG_NAME, 'textarea')



                    main_msg = f'Hi {name},\n{msg}'
   
                    text.send_keys(msg)
                    time.sleep(2)
                    send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
                    driver.execute_script("arguments[0].click();", send)


                except:
                    close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
                    driver.execute_script("arguments[0].click();", close)
                

    except:

        more = driver.find_element(By.XPATH,"//button[@aria-label='More actions']")
        driver.execute_script("arguments[0].click();", more)
        time.sleep(7)
        all_btns = driver.find_elements(By.XPATH, "//div[@role='button']")
        for btn in all_btns:
            if btn.text == 'Connect':              
                driver.execute_script("arguments[0].click();", btn)
                try:
                    add_note = driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
                    driver.execute_script("arguments[0].click();", add_note)
                    time.sleep(3)

                    text = driver.find_element(By.TAG_NAME, 'textarea')
                    main_msg = f'Hi {name},\n{msg}'
  
                    text.send_keys(msg)
                    time.sleep(2)
                
                    send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
                    driver.execute_script("arguments[0].click();", send)


                except:
                    close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
                    driver.execute_script("arguments[0].click();", close)
               
    finally:
        pass 

print('All Links done!')