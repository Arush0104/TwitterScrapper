#Kindly install all these modules
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo

tweets_list = []
name = input("Enter Username")

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(name).get_items()):
    if i > 1000:
        break
    tweets_list.append(
        [tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])


df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'URL', 'ReplyCount','retweetCount','Language','Source,','LikeNumber'])
print(df)
df.to_csv()

client = pymongo.MongoClient("mongodb+srv://arush0104:123@cluster0.m0edrgj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db = client['Scrapper']
collection = db['Scrapper']
df.reset_index(inplace=True)
data_dict = df.to_dict("records")
# Insert collection
collection.insert_many(data_dict)

