import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://www.instagram.com/")
 
while "1" != input("press 1 when signed in: "):
    pass

number_of_messages=input("How many messages do you want to send?")
message=input("What is the message you want to send?")
position_on_the_list=input("What's the position of the person you want to spam on your chat list?")

driver.get("https://www.instagram.com/direct/inbox/")

sleep(5)

buttons = driver.find_elements_by_class_name("rOtsg")
buttons[int(position_on_the_list)-1].click()

sleep(2)

textarea = driver.find_element_by_tag_name("textarea")

count=int(number_of_messages)

while count>0:
    textarea.send_keys(message)
    driver.find_element_by_xpath('//button[normalize-space()="Send"]').click()
    count-=1

sleep(10)
driver.close()