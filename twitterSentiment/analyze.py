import tweepy
from textblob import TextBlob
# testing textblob

wiki = TextBlob("I am always angry if I do not eat on time")

# finding out the tags
print(wiki.tags)

#finding out the words
print(wiki.words)

#findingoutthesentimate
print(wiki.sentiment.polarity)