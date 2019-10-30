import tweepy
from tweepy import Cursor
import unicodecsv
from unidecode import unidecode
import json
import datetime

####input your credentials here
consumer_key = 'VWumRz5dQcduRj9FQel4f8qcm'
consumer_secret = 'EfXmu5vfFd00t3BfX42JbsaNOf3LCC3Is4je5hQfpGuCmvhjDX'
access_token = '965507672945713152-bZzrscE41RQWctVkm86uGuAv13oo1uB'
access_token_secret = 'PGvvgnXM5omK0tTQZdtUi3KSLjs6MnjXZx09IVQgqiSST'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open('sports.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#PL",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info)
        
with open('Brexit.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#brexit",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info1 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info1)
        
with open('Syria.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#syria",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info2 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info2)       
       
with open('oscars.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#oscars",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info3 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info3)

with open('forbes.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#forbes",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info4 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info4)
        
with open('californiafires.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#californiafires",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info5 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info5)

with open('trump.csv', 'wb') as file:
    writer = unicodecsv.writer(file, delimiter = ',', quotechar = '"')
    writer.writerow(["Tweet","User Name","Location"])
    count = 1
    i = 1
    mydict = {}
    for tweet in tweepy.Cursor(api.search,q="#trump",count=100,
                         lang="en").items(1000):
        print (tweet.author.name)
        #mydict.update({"_id": i, "Tweet": unidecode(tweet.text), "Author Name": tweet.author.screen_name, "Author Location": tweet.author.location }) 
        #collection.insert(mydict)
        i=i+1
        tweet_info6 = [
                unidecode(tweet.text),
                tweet.author.screen_name,
                tweet.author.location
             ]
        writer.writerow(tweet_info6)
