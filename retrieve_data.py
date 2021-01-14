import tweepy
from tweepy import OAuthHandler
import credentials
import pandas as pd
import csv
import json

# authentication 
auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Politicians
# Joe Biden, Kamala Harris, Mitch McConnell, Mike Pence, AOC, Bernie Sanders, Andrew Yang
screen_names = [ "JoeBiden", "KamalaHarris", "senatemajldr", "Mike_Pence", "BernieSanders", "AndrewYang"]

# retrieve user timeline and store it in dictionary
tweet_dictionary = {}
for screen_name in screen_names:
    # retrieve more tweets from Mike Pence
    if screen_name == "Mike_Pence":
        tweets = api.user_timeline(screen_name, count=300, exclude_replies=True, include_rts=False, tweet_mode='extended')
        all_tweets = []
        all_tweets.extend(tweets)
        # retrieve id of oldest tweet so far
        oldest_id = tweets[-1].id
        while True:
            # retrieve tweets that are older than or equal to the speicified id in max_id
            tweets = api.user_timeline(screen_name, count=300, exclude_replies=True, max_id = oldest_id - 1, include_rts=False, tweet_mode='extended')
            if len(all_tweets) > 150:
                break
            oldest_id = tweets[-1].id
            all_tweets.extend(tweets)
        print(screen_name, len(all_tweets))
        tweet_dictionary[screen_name] = all_tweets   
    else:
        tweets = api.user_timeline(screen_name, count=300, exclude_replies=True, include_rts=False, tweet_mode='extended')
        print(screen_name, len(tweets))
        tweet_dictionary[screen_name] = tweets

joeBidenTweets = tweet_dictionary["JoeBiden"]
print(joeBidenTweets[0])
# df = pd.DataFrame(joeBidenTweets[0], columns = ['id', 'created_at', 'full_text'])
# print(df)
# df = pd.DataFrame(joeBidenTweets, )

with open('tweets.csv', 'w', newline='') as f:
    tweet_writer = csv.writer(f)
    tweet_writer.writerow(['Tweeter', 'Tweet ID', 'Tweet Time', 'Tweet Text', 'Topics'])
    for key in tweet_dictionary:
        for tweet in tweet_dictionary[key]:
            tweet_writer.writerow([key, tweet.id, tweet.created_at, tweet.full_text, ''])

# for info in tweet_dictionary["JoeBiden"]:
#     print("ID: {}".format(info.id))
#     print(info.created_at)
#     print(info.full_text)
#     print("\n")



    

#----------------------code for retreieving access token---------------#    
# try:
#     redirect_url = auth.get_authorization_url()
#     print(redirect_url)
# except tweepy.TweepError:
#     print("Error! Failed to request token")

# user_pin_input = input("Enter pin: ")
# auth.get_access_token(user_pin_input)
# print(auth.access_token, auth.access_token_secret)




