from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""""
-----------------Requirements----------------
- pip install selenium
- Must have stable and fast internet before starting this script.

"""
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@name='session_password']")

username.send_keys('username')
password.send_keys('password')
time.sleep(2)

submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()



#***************** Enter your message here ***********************

msg = """I'll glad to join your network"""
# set page range here starting from 1 and ending less than 100
for x in range(1,3):

    print(f'Sending connect on page: {x}')

    # Enter your required linkedIn url here with required filters 
    # Must set f string link this  url bellow
    # Run the code and watch the show

    driver.get(f"https://www.linkedin.com/search/results/people/?keywords=tableau%20scientist&origin=SWITCH_SEARCH_VERTICAL&page={x}&searchId=f06d76c8-901c-4d3d-8a61-e744a0230b81&sid=w5!")
    time.sleep(7)

    all_buttons = driver.find_elements(By.TAG_NAME,"button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2.5)
        
        # add_note = driver.find_element(By.XPATH,"//button[@aria-label='Add a note']")
        # driver.execute_script("arguments[0].click();", add_note)
        # time.sleep(7)

        # text = driver.find_element(By.TAG_NAME, 'textarea')
        # text.send_keys(msg)
        # time.sleep(1.5)
        # send = driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
        # driver.execute_script("arguments[0].click();", send)


        
        close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
       
print('All pages are done.')
driver.quit()
