import tweepy #This module or package is to connect through Twitter API.
from textblob import TextBlob # This module is useful to give the polarity score of the tweets.
consumer_key = 'Y12HRyJy7HeqqWvH50e1vfKoH'
# These are the keys to authenticate Twitter API
consumer_secret = 'HGpIIbhda35iRQhKJDpDs801CibZ8jgO56KjLPfD7neSYTmqre'
#These keys will be regenerate from the developer account.
access_token = '1423834823441883137-WabLIW4m5klKKfoEfq5XWi1T1K2h7e'
access_token_secret = 'YNAaxtsjtYdcpWVOJDM53STbh528PpliEqkTjogTJXsZo'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
# This will check whether the consumer_key and consumer_secret_key was correct.If correct means it will authenticate.
# Thats why we are using OAuthHandler built in functions.
auth.set_access_token(access_token,access_token_secret)
#And we are checking that access token and acces_token_secret is correct .If all the four are correct means it will enter into twitter API.
api = tweepy.API(auth)#This will connect through the twitter API.
public_tweets = api.search("virat kohli")
#Now we can search for the public tweets to find the sentiment.
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text) # This will give you the polarity score.
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print("POSITIVE")
    elif analysis.sentiment[0]<0:
        print("NEGATIVE")
    else:
        print("NEUTRAL")
