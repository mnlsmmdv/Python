"""
Name: Ahmed Affaan                                  
Title: twitter_bot.py                               
Date: 17/10/2021                                    
Country: Republic of Maldives                       
Code version: 3.8.10                                
Description: Twitter bot version 01                 
Note: Uncomment codes to execute and comment 
them when not in use.                         
"""

# Program start
# Importing tweepy module
import tweepy

# Credentials for the API keys will go here
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

# Setting a variable for the API handlers
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

# Class defined to execute the like function of tweepy bot
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print("Tweet Found!")
        print(f"{tweet.author.screen_name} - {tweet.text}")
        if tweet.in_reply_to_status_id is None and not tweet.favorited:
            try:
                print("Attempting Like...")
                api.create_favorite(tweet.id)
                print("Tweet successfully liked!")
            except Exception as err:
                print(err)

# Class variable defined
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["#IndiaOut", "Maldives"], languages=["en"])

# Program end
