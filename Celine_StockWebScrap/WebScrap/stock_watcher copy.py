from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import date

''' 
create a webdriver chrome object by passing the path of "chromedriver.exe" file.(do not include .exe in the path).
'''
options_chrome = webdriver.ChromeOptions()

#anti-window open
options_chrome.add_argument('--headless')
#anti-bot
options_chrome.add_argument("--disable-blink-features")
options_chrome.add_argument("--disable-blink-features=AutomationControlled")
#anti-crash page
options_chrome.add_argument('--no-sandbox')    
#logging-disable
options_chrome.add_argument('--log-level=3')

chrome = webdriver.Chrome('./WebScrap/chromedriver.exe', options=options_chrome)

# Input Parameter
        
currency_target ={
    'MYR' : 1851.73,
    'IDR' : 14626.60,
    'CNY' : 6.69,
    'EUR' : 0.94,
    'GBP' : 0.8
}
while True:
    key_currency = input("Please input currency code :")
    if key_currency not in currency_target.keys():
        key_currency = input("Please re-input currency code :")
    else:
        break

# stock_code = ['TSLA','AAPL','FB','NFLX', 'EFX', 'FIS', 'IRM', 'LH', 'AMAT', 'NTAP']
stock_code = []
stock_input = input("Please input stock code (CAPITALIZE ONLY): ")
stock_code.append(stock_input)

while stock_input.lower() != 'done':
    stock_input = input("Please input stock code (CAPITALIZE ONLY): ")
    if stock_input.lower() != 'done':
        stock_code.append(stock_input)

try:
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")

    print(f"Stock Price @ {today} {current_time}")
    
    for stock_pick in stock_code:
        # Get Stock Price
        link = "https://finance.yahoo.com/quote/"+stock_pick
        chrome.get(link)
        tbl = chrome.find_element(by=By.XPATH,value=f"//fin-streamer[@data-test=\"qsp-price\"]").get_attribute('outerHTML')
        tbl = tbl.split()
        data_stock = tbl[10]
        data_stock = data_stock.replace("value=","")
        data_stock = data_stock.replace("\"","")
        data_stock = float(data_stock)
        data_currency = data_stock*currency_target[key_currency] 

        print(f"The {stock_pick} price is ${data_stock} equals to {key_currency} {data_currency}")
        
finally:
    chrome.quit()