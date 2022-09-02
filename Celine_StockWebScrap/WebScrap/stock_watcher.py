from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import re
''' 
create a webdriver chrome object by passing the path of "chromedriver.exe" file.(do not include .exe in the path).
'''
options_chrome = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\ZENI\\AppData\\Local\\Google\\Chrome\\User Data")
# options.add_argument('profile-directory=Profile 3')
#anti-window open
options_chrome.add_argument('--headless')
#anti-bot
options_chrome.add_argument("start-maximized")
options_chrome.add_argument("--disable-blink-features")
options_chrome.add_argument("--disable-blink-features=AutomationControlled")
#anti-crash page
options_chrome.add_argument('--no-sandbox')    
#logging-disable
options_chrome.add_argument('--log-level=3')
chrome = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe', options=options_chrome)

# Input Parameter
stock_code = 'TSLA'
currency_target = 'MYR'


try:
    while True:
        # Get Stock Price
        link = "https://finance.yahoo.com/quote/"+stock_code
        chrome.get(link)
        tbl = chrome.find_element(by=By.XPATH,value=f"//fin-streamer[@data-symbol=\"{stock_code}\"]").get_attribute('outerHTML')
        tbl = tbl.split()
        data_stock = tbl[10]
        data_stock = data_stock.replace("value=","")
        data_stock = data_stock.replace("\"","")
        data_stock = float(data_stock)
        # chrome.close()
        time.sleep(30)
        
        # Convert Currency
        link = f"https://www.xe.com/currencyconverter/convert/?Amount={str(data_stock)}&From=USD&To={currency_target}"
        chrome.get(link)
        tbl = chrome.find_element(By.CSS_SELECTOR,".result__BigRate-sc-1bsijpp-1.iGrAod").get_attribute('outerHTML')
        pattern = "iGrAod\">(.*?)<"
        tbl = re.search(pattern, tbl).group(1)
        data_currency = float(tbl.replace(",","")) 

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # chrome.close()

        print(f"The {stock_code} price is ${data_stock} equals to {currency_target} {data_currency} @ {current_time}")
        time.sleep(30)
finally:
    chrome.quit()