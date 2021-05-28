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

requests_to_be_deleted=input("How many pending requests do you want to delete?")

buttons=driver.find_elements_by_class_name("_8-yf5")

for button in buttons:
    if button.get_attribute("aria-label") == "Activity Feed":
        button.click()
        sleep(5)

button=driver.find_elements_by_class_name("eKc9b")
print("Moving to the Follow Requests Tab ....")
sleep(1)
button[0].click()
print("All your follow requests are listed here! All pending follow requests will be deleted one by one!")
sleep(2)

count=int(requests_to_be_deleted)

while count>=0:
    button = driver.find_element_by_xpath('//button[normalize-space()="Delete"]')
    print("Deleting a request.......")
    button.click()
    print("Request Deleted.")
    sleep(2)
    count-=1


print("Your pending follow requests are now deleted!! Enjoy :)")
driver.close()