# Update and Store API and Key Access within the same folder
# Go get in https://developer.twitter.com/en
# Click Developer Portal
# Activated The Developer used and confirm your email
# Masuk ke App Setting and Authentication set up
# Read Write, Native, Callback URI = https://www.google.com/, Website URL = https://www.google.com/
# Go get the API KEY, API Key Secret, Access Token, Access Secret Token and store in excel
# Upgrade the Essential into Elevated https://developer.twitter.com/en/portal/dashboard click Products -> apply Elevated
# Ready to use!

import tweepy
import time
import pandas as pd
import random

def run_job (
    API_key,
    API_secret_key,
    access_token,
    access_secret,
    id,
    username_to_follow = "",
    username_to_reply = "",
    reply_message = "",
    like = False,
    retweet = False,
    reply = False,
    follow = False):
    
    try:
        # input API Key - API Secret Key
        auth = tweepy.OAuthHandler(API_key, API_secret_key)

        # input Access Token - Access Token Secret
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth, 
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

        if follow:
            if username_to_follow == "":
                return print("You must input the username to follow!")
            else:
                list_follow = username_to_follow.split()
                for username in list_follow:
                    print(f"---Following: {username}")
                    api.create_friendship(username)
                    time.sleep(5)
        
        if retweet:
            api.retweet(id)
            print("---Retweet---")
            time.sleep(1)
        
        if like:
            api.create_favorite(id)
            print("---Liked---")
            time.sleep(1)

        if reply:
            if reply_message == "":
                return print("Input your message status!")
            elif username_to_reply == "":
                return print("Input reply username!")
            else:
                # api.update_status(reply_message+" @"+username_to_reply, in_reply_to_status_id = id)
                api.update_status(reply_message, in_reply_to_status_id = int(id), auto_populate_reply_metadata=True)
                print("---Replied---")

    except tweepy.TweepError as e:
        print(e.reason)

data = pd.read_excel("db.xlsx")
data_reply = pd.read_excel("db.xlsx",sheet_name="Sheet2",header=None)

# How to use
# 1. Find the Tweet ID and insert in ID Parameter -> ini untuk retweet, likes, reply
# 2. Jika follow true -> please fill in the username to follow and split with space without "@"
# 3. Jika reply True -> please fill in the username to reply

for user in range(len(data)):
    
    API_key = data['APIkey'][user]
    API_secret_key = data['APISKey'][user]
    AccessToken = data['AccessToken'][user]
    AccessSecret = data['AccessTS'][user]
    print(f"---Working on account name: {data['username'][user]}")
    run_job(API_key=API_key,
        API_secret_key=API_secret_key, 
        access_token=AccessToken, 
        access_secret=AccessSecret,
        id="1568963167635779584",
        username_to_follow="PRJCTWhitelist Kuroki_NFT",
        username_to_reply="Kuroki_NFT",
        reply_message= data_reply[0][random.randint(0, len(data_reply))],
        like=True,
        retweet=True,
        reply=True,
        follow=True
        )
    time.sleep(random.randint(10, 15))