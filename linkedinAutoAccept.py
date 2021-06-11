import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")
# delete this after every month
 
while "1" != input("press 1 when signed in: "):
    pass

driver.get("https://www.linkedin.com/mynetwork/")

sleep(4)

buttons = driver.find_elements_by_class_name("invitation-card__action-btn")

sleep(2)       
for button in buttons:
    word= button.get_attribute("aria-label").split(" ")[0]
    
    if(word == "Accept"):
        print("Accepting request...")
        button.click()
        print("Accepted")
        sleep(2)

 
driver.close()
