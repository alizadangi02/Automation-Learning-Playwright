# imports sync_playwright and uses it to launch a browser, navigate to Google, print the page title, and then close the browser.
from playwright.sync_api import sync_playwright


#with statement safely starts and stops the playwright for us.
#p gives access to the browser.
with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False) #headless=False to see the browser window
    page = browser.new_page()
    page.goto("https://www.google.com") #navigates to the specified URL
    print(page.title()) #prints the title of the page to the console. This should output "Google" if the navigation was successful.
    browser.close() #closes the browser after the operations are completed.

#to run: python first_test.py