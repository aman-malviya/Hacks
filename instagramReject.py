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

buttons=driver.find_elements_by_class_name("_8-yf5")

for button in buttons:
    if button.get_attribute("aria-label") == "Activity Feed":
        button.click()
        sleep(10)

button=driver.find_elements_by_class_name("eKc9b")
print("Moving to the Follow Requests ...")
button[0].click()
sleep(1)
print("All your follow requests are listed here! All pending follow requests will be deleted one by one!")
sleep(2)

buttons = driver.find_elements_by_xpath('//button[normalize-space()="Delete"]')

sleep(2)       
for button in buttons:
    print("Deleting a request")
    button.click()
    print("Deleted a request")
    sleep(2)


print("All your pending follow requests are now deleted!! Enjoy :)")
driver.close()