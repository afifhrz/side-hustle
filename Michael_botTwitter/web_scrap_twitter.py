# pip install selenium
# Check Chrome Version
# Download Chromium https://chromedriver.chromium.org/home
# Edit System Env -> System Variables -> 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import random
from time import sleep

def run_job (
    myuser,
    mypass,
    url_tweet,
    username_to_follow = [],
    reply_tweet = "",
    like = False,
    retweet = False,
    reply = False,
    follow = False):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--start-maximized")
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    chrome.set_page_load_timeout(30)

    chrome.get("https://twitter.com/i/flow/login")
    username =  WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="text"]'))
    )
    username.send_keys("%s" % (myuser))

    sleep(3)  # Long enough to see the name was typed

    chrome.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div').click()

    password =  WebDriverWait(chrome, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="password"]'))
    )
    password.send_keys("%s" % (mypass))
    sleep(2)

    chrome.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div.css-1dbjc4n > div > div > div > div').click()
    sleep(2)

    chrome.execute_script('window.location="'+url_tweet+'";')
    sleep(3)

    # check parameter
    if follow:
        if username_to_follow == []:
            return print("You must input the username to follow!")

    # to like
    if like:
        chrome.find_element(By.XPATH, '''//div[@data-testid="like"]''').click()
        print("---Liked---")
        sleep(2)

    # to retweet
    if retweet:
        chrome.find_element(By.XPATH, '''//div[@data-testid="retweet"]''').click()
        sleep(2)

        chrome.find_element(By.XPATH, "//*[@data-testid='retweetConfirm']").click()
        print("---Retweeted---")
        sleep(2)

    # to reply
    if reply:
        reply = chrome.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > section > div > div > div:nth-child(1) > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1f1sjgu").click()
        actions = ActionChains(chrome)
        actions.send_keys("%s" % (reply_tweet+" "))
        actions.perform()
        sleep(3)

        chrome.find_element(By.XPATH, '''//div[@data-testid="tweetButtonInline"]/div/span/span''').click()
        sleep(8)
        print("---Replied---")

    # to follow
    if follow:
        for user in username_to_follow:
            chrome.execute_script('window.location="https://twitter.com/'+user+'";')
            sleep(5)
            chrome.find_element(By.XPATH, '''//div[@data-testid="placementTracking"]''').click()
            sleep(2)
            print(f"---Followed: {user}")

    chrome.quit()

data = pd.read_excel('username.xlsx', sheet_name='Sheet1')
data_reply = pd.read_excel('username.xlsx', sheet_name='Sheet2',header=None)

url_tweet = '/mbdcollabs/status/1572209365444349952'
username_to_follow = ['moonbirdsdyn','pinky2000112','SupercuteNFT','moonbirdsdyn']
start_user_index = 0

for user in range(start_user_index,len(data)):
    print(f"---Working on account name: {data['username'][user]}")
    myuser = data['username'][user]
    mypass = data['pass'][user]
    reply_tweet = data_reply[0][random.randint(0, len(data_reply)-1)]
    run_job(
        myuser,
        mypass,
        url_tweet,
        username_to_follow,
        reply_tweet,
        like = True,
        retweet = True,
        reply = True,
        follow = True
        )
    sleep(random.randint(10, 15))