from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import tweepy
import credentials
import pandas as pd
import json


# authentication 
auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Politicians
# Joe Biden, Kamala Harris, Mitch McConnell, Mike Pence, AOC, Bernie Sanders, Andrew Yang
screen_names = [ "JoeBiden", "KamalaHarris", "senatemajldr", "Mike_Pence", "BernieSanders", "AndrewYang"]

# retrieve user timeline
all_tweets = []
for screen_name in screen_names:
    if screen_name == "Mike_Pence":
        tweets = api.user_timeline(screen_name, count=300, exclude_replies=True, include_rts=False, tweet_mode='extended')
        all_tweets = []
        all_tweets.extend(tweets)
        oldest_id = tweets[-1].id
        while True:
            tweets = api.user_timeline(screen_name, count=300, exclude_replies=True,max_id = oldest_id - 1, include_rts=False, tweet_mode='extended')
            if len(all_tweets) > 200:
                break
            oldest_id = tweets[-1].id
            all_tweets.extend(tweets)
            # print('N of tweets downloaded till now {}'.format(len(all_tweets)))
        print(screen_name, len(all_tweets))
        for info in all_tweets:
            print("ID: {}".format(info.id))
            print(info.created_at)
            print(info.full_text)
            print("\n")
        
    else:
        tweets = api.user_timeline(screen_name, count=300, exclude_replies=True, include_rts=False, tweet_mode='extended')
        print(screen_name, len(tweets))
        for info in tweets:
            print("ID: {}".format(info.id))
            print(info.created_at)
            print(info.full_text)
            print("\n")



# for k in vars(joeBidenTimeline).keys():
#     print(k)


    
    


# try:
#     redirect_url = auth.get_authorization_url()
#     print(redirect_url)
# except tweepy.TweepError:
#     print("Error! Failed to request token")

# user_pin_input = input("Enter pin: ")
# auth.get_access_token(user_pin_input)
# print(auth.access_token, auth.access_token_secret)




