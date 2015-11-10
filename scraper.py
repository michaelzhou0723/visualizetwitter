import tweepy
	
def scrape(query,total,collection):
	consumer_key = ''		# Twitter Consumer Key
	consumer_secret = ''	# Twitter Consumer Secret
	auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
	api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
	for tweet in tweepy.Cursor(api.search, q=query,lang='en',count=100).items(total):
		result = collection.insert_one(
			{
				'text': tweet.text,
				'id': tweet.id,
				'created_at': tweet.created_at
			}
		)
		if tweet.coordinates:
			collection.update_one(
				{'_id': result.inserted_id},
				{
					'$set': {
						'coordinates': tweet.coordinates
					}
				}
			)
		if hasattr(tweet,'retweeted_status'):
			collection.update_one(
				{'_id': result.inserted_id},
				{
					'$set': {
						'original': tweet.retweeted_status.id
					}
				}
			)
	
		
	
	
	
