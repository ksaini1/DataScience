import pymongo
from pymongo import MongoClient
import json
import twitter
from pprint import pprint


CONSUMER_KEY="VWumRz5dQcduRj9FQel4f8qcm"
CONSUMER_SECRET="EfXmu5vfFd00t3BfX42JbsaNOf3LCC3Is4je5hQfpGuCmvhjDX"
OAUTH_TOKEN="965507672945713152-bZzrscE41RQWctVkm86uGuAv13oo1uB"
OAUTH_TOKEN_SECRET="PGvvgnXM5omK0tTQZdtUi3KSLjs6MnjXZx09IVQgqiSST"


auth=twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
twitter_api=twitter.Twitter(auth=auth)



client=MongoClient()
db=client.tweet_db
tweet_collection=db.tweet_collection
tweet_collection.create_index([("id",pymongo.ASCENDING)],unique=True)


count=50
q="iphone11"
search_results=twitter_api.search.tweets(count=count,q=q)
#pprint(search_results['search_metadata'])


statuses=search_results["statuses"]

since_id_new=statuses[-1]['id']

for statues in statuses:
       try:
              tweet_collection.insert(statues)
       except:
              pass
       
       
tweet_cursor=tweet_collection.find()
print(tweet_cursor.count())
user_cursor=tweet_collection.distinct("user.id")
print(len(user_cursor))

for document in tweet_cursor:
       try:
              print('-----')
              print('name:-',document["user"]["name"])
              print('text:-',document["text"])
              print('Created Date:-',document["created_at"])
       except:
              print("Error in Encoding")
              pass
