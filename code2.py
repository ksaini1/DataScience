import tweepy
from tweepy import Cursor
import unicodecsv
from unidecode import unidecode
from pymongo import MongoClient
import json
from pymongo import Connection
import datetime

####input your credentials here
consumer_key = 'VWumRz5dQcduRj9FQel4f8qcm'
consumer_secret = 'EfXmu5vfFd00t3BfX42JbsaNOf3LCC3Is4je5hQfpGuCmvhjDX'
access_token = '965507672945713152-bZzrscE41RQWctVkm86uGuAv13oo1uB'
access_token_secret = 'PGvvgnXM5omK0tTQZdtUi3KSLjs6MnjXZx09IVQgqiSST'

connection = Connection('localhost', 27017)
db = connection.TwitterStream
db.tweets.ensure_index("id", unique=True, dropDups=True)
collection = db.tweets

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#####United Airlines
# Open/Create a file to append data
#with open('tweetstry.csv') as file:
with open('tweets.csv', 'wb') as file:
    #writer = unicodecsv.writer(file)
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    # Write header row.
    writer.writerow(["Tweet","User Name","Location"])

    for tweet in tweepy.Cursor(api.search,q="#iphone11",count=100,
                           lang="en").items():
       print (tweet.author.name)
       print(tweet.author.screen_name)


       tweet_info = [
           unidecode(tweet.text),
           tweet.author.screen_name,
           tweet.author.location

       ]
      #tweettext= []
      #tweettext= tweet.entities.get('text', None)
      #if (tweetext != None):
      #   for i in range(len(tweettext)):
      #       tweettext.append(unidecode(tweettext[i]['type']))
      #tweetinfo=[join(tweettext), len(tweettext)]
collection.save(tweet_info)
       #tweetinfo=tweet.entities.get('text', None)
writer.writerow(tweet_info)

