import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://web.whatsapp.com/")
 
while "1" != input("press '1' when signed in: "):
    pass

sleep(5)

name=input("Enter the name of person you want to spam (spell exactly the same): ")
number_of_messages=input("How many messages do you want to send?")
message=input("What is the message you want to send?")

buttons = driver.find_elements_by_class_name("_35k-1")

for button in buttons:
    if button.get_attribute("title") == name:
        button.click()
        sleep(1)
        break

sleep(2)

count=int(number_of_messages)

while count>0:
    driver.find_elements_by_class_name("_2_1wd ")[1].send_keys(message)
    driver.find_element_by_class_name("_1E0Oz").click()
    count-=1

sleep(5)
driver.close()