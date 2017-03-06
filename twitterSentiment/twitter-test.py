####
# GETS THE FIRST 15 tweets about a perticular word and gievs sentiment analysis
####
import tweepy
from textblob import TextBlob

consumer_key =  '7ToyVXoOUcfpXP1abu1Y5F8O0'
consumer_secret = 'vWaWjHIg5zLcp0rywhPuJydhNC9BEMBWlgPEdbf9Fl4FWx5CyH'

access_token = '838773351841689600-bAIGlh31iUNxDPvVSr6vvpCOI2VIqiN'
access_token_secret = 'aKbRll5qMAy9VM7KDPs8WyS8cQDnoXsPoQwPcELofaywt'

#authenticates
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

#Retrieve Tweets related to Trump
public_tweets = api.search('Trump')



for tweet in public_tweets:
    print(tweet.text)

    #Perform Sentiment Analysis on Tweets ( POLARITY IS HOW POSITIVE OR NEGATIVE A TEXT IS
    #subjectivity measures opnion vs fact
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
