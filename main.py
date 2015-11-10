from pymongo import MongoClient
from scraper import scrape
import preprocess

if __name__ == '__main__':
	client = MongoClient()
	collection = client.twitter.tweets
	scrape('#Christmas',150000,collection)
	preprocess.count_date(collection.find())
	preprocess.analyze_term(collection.find())
	preprocess.to_geojson(collection.find({'coordinates': {'$exists':1}}))
	preprocess.construct_retweets_graph(collection.find())
	client.close()
	