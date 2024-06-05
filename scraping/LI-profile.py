from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv



username = "talhanadeem718@gmail.com"
password = "#LItalha@782"
msg = 'hey How are you.'

with open('Data/file_name.csv', 'r') as f:
    reader = csv.DictReader(f)

    links = []
    for row in reader:
        links.append(row['Link'])
print(len(links)+ '\nProgram sarted. Now wait.....')
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
for link in links:
    driver.get(link)

    time.sleep(5)
    try:
        cnt_btn = driver.find_elements(By.TAG_NAME, 'button')
        for btn in cnt_btn:
            if btn.text == 'Connect':
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
                add_note = driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
                driver.execute_script("arguments[0].click();", add_note)
                time.sleep(7)

                text = driver.find_element(By.TAG_NAME, 'textarea')
                text.send_keys(msg)
                time.sleep(1.5)
                send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
                driver.execute_script("arguments[0].click();", send)


                
                close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
                driver.execute_script("arguments[0].click();", close)
                time.sleep(2)

    except:

        more = driver.find_element(By.XPATH,"//button[@aria-label='More actions']")
        driver.execute_script("arguments[0].click();", more)
        time.sleep(7)
        all_btns = driver.find_elements(By.XPATH, "//div[@role='button']")
        for btn in all_btns:
            if btn.text == 'Connect':              
                driver.execute_script("arguments[0].click();", btn)
                add_note = driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
                driver.execute_script("arguments[0].click();", add_note)
                time.sleep(7)

                text = driver.find_element(By.TAG_NAME, 'textarea')
                text.send_keys(msg)
                time.sleep(1.5)
                send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
                driver.execute_script("arguments[0].click();", send)


                
                close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
                driver.execute_script("arguments[0].click();", close)
                time.sleep(2)
    else:
        pass 

print('All Links done!')