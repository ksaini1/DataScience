import tweepy
from tweepy import Cursor
import unicodecsv
from unidecode import unidecode
from pymongo import MongoClient
import json
import datetime

####input your credentials here
consumer_key = 'VWumRz5dQcduRj9FQel4f8qcm'
consumer_secret = 'EfXmu5vfFd00t3BfX42JbsaNOf3LCC3Is4je5hQfpGuCmvhjDX'
access_token = '965507672945713152-bZzrscE41RQWctVkm86uGuAv13oo1uB'
access_token_secret = 'PGvvgnXM5omK0tTQZdtUi3KSLjs6MnjXZx09IVQgqiSST'

client=MongoClient()
db=client.sports
pl=db.pl
pl.create_index([("id",pymongo.ASCENDING)],unique=True)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open('sports.csv', 'wb') as file:
    #writer = unicodecsv.writer(file)
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    # Write header row.
    writer.writerow(["Tweet","User Name","Location"])

    for tweet in tweepy.Cursor(api.search,q="#PL",count=100,
                           lang="en").items():
       print (tweet.author.name)
       print(tweet.author.screen_name)


       tweet_info = [
           unidecode(tweet.text),
           tweet.author.screen_name,
           tweet.author.location

       ]
       pl.insert(tweet_info)
      #tweettext= []
      #tweettext= tweet.entities.get('text', None)
      #if (tweetext != None):
      #   for i in range(len(tweettext)):
      #       tweettext.append(unidecode(tweettext[i]['type']))
      #tweetinfo=[join(tweettext), len(tweettext)]

       #tweetinfo=tweet.entities.get('text', None)
writer.writerow(tweet_info)


