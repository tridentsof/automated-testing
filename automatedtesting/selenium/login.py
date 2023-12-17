# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from datetime import date, datetime

def getTimestamp():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (time + '\t')

def currentTime ():
    today = date.today()
    print("Today's date:", today)

# Start the browser and login with standard_user
def login (user, password):
    print (f'{getTimestamp()} Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    print (f'{getTimestamp()} Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    #login test
    driver.find_element("css selector", "input#user-name").send_keys(user)
    driver.find_element("css selector", "input#password").send_keys(password)
    driver.find_element("css selector", "input#login-button").click()
    print (f'{getTimestamp()} Login with user name {user} and password {password} successfuly')
    return driver

def add_item_to_cart(driver, itemNumber):
    print (f'{getTimestamp()} Adding items to cart')

    itemElements = driver.find_elements("css selector", "div.inventory_item")
    for element in itemElements:
        descriptionItem = element.find_element("css selector", "div.inventory_item_name").text
        element.find_element("css selector", "button[id^='add-to']").click()
        print (f'{getTimestamp()} {descriptionItem} was added to cart')

    print (f'{getTimestamp()} Total items was added {itemNumber}')

def remove_item_from_cart(driver, itemNumber):
    print (f'{getTimestamp()} Removing items from cart')
    driver.find_element("css selector", "a.shopping_cart_link").click()
    itemElements = driver.find_elements("css selector", "div.cart_item")
    itemRemoved = 0
    for element in itemElements:
        descriptionItem = element.find_element("css selector", "div.inventory_item_name").text
        element.find_element("css selector", "button[id^='remove-']").click()
        itemRemoved += 1
        print (f'{getTimestamp()} {descriptionItem} was removed from cart')
        if(itemRemoved > itemNumber):
            break
    
    print (f'{getTimestamp()} Total items was removed {itemNumber}')

if __name__ == "__main__": 
    itemNumber = 6 
    testUsername = 'standard_user' 
    testPassword = 'secret_sauce'
    currentTime()
    driver = login(testUsername, testPassword) 
    add_item_to_cart(driver, itemNumber)
    remove_item_from_cart(driver, itemNumber)
    print(f'{getTimestamp()} Selenium tests are all successfully completed!') 
