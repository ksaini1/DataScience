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
syria=db.syria
syria.create_index([("id",pymongo.ASCENDING)],unique=True)
sports=db.sports
sports.create_index([("id",pymongo.ASCENDING)],unique=True)
brexit=db.brexit
brexit.create_index([("id",pymongo.ASCENDING)],unique=True)
oscars=db.oscars
oscars.create_index([("id",pymongo.ASCENDING)],unique=True)
forbes=db.forbes
forbes.create_index([("id",pymongo.ASCENDING)],unique=True)
trump=db.trump
trump.create_index([("id",pymongo.ASCENDING)],unique=True)
californiafires=db.californiafires
californiafires.create_index([("id",pymongo.ASCENDING)],unique=True)



count=10
q="#syria"
p="#PL"
r="#brexit"
s="#oscars"
t="#forbes"
u="#trump"
v="#californiafires"


search_syria=twitter_api.search.tweets(count=count,q=q,lang="en")
#print(ssarch_results['search_metadata)


statsyria=search_syria["statuses"]

since_id_new=statsyria[-1]['id']

for statues in statsyria:
       try:
              syria.insert(statues)
       except:
              pass
       
       
tweet_cursor=syria.find()
print(tweet_cursor.count())
user_cursor=syria.distinct("user.id")
print(len(user_cursor))


