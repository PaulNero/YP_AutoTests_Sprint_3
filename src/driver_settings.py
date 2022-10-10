from selenium import webdriver

def chrome_browser():
    driver = webdriver.Chrome(executable_path="/Users/pavelnerobov/Documents/WebDriver/chromedriver")
    return driver

def firefox_browser():
    driver = webdriver.Firefox()
    return driver

def safari_browser():
    driver = webdriver.Safari()
    return driver