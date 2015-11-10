from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import regexp
import json
import math
import string

def count_date(tweets):
	c = Counter()
	dates = [str(t['created_at'])[:10] for t in tweets]
	c.update(dates)
	data = [item for item in c.items()]
	data.sort()
	with open('json/trend.json','w') as f:
		json.dump(data,f)
		
def analyze_term(tweets):
	c = Counter()
	tokenizer = regexp.RegexpTokenizer('@\w+|\w{3,}')
	stop = stopwords.words('english')+list(string.punctuation)+['rt','via']
	for tweet in tweets:
		tokenized = tokenizer.tokenize(tweet['text'])
		processed = [t.lower() for t in tokenized if t.lower() not in stop]
		c.update(processed)
	with open('json/freq.json','w') as f:
		transformed = []
		for value in c.most_common(50):
			transformed.append([value[0],int(math.sqrt(value[1]))])
		json.dump(transformed,f)
		
def to_geojson(tweets):
	geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
	for tweet in tweets:
		feature = {
            "type": "Feature",
            "geometry": tweet['coordinates'],
        }
		geo_data['features'].append(feature)
	with open('json/geo.json','w') as f:
		json.dump(geo_data,f)
		
def construct_retweets_graph(tweets):
	graph = []
	ids = []
	most_retweeted = []
	for tweet in tweets:
		if 'original' in tweet:
			ids.append((tweet['id'],tweet['original']))
	original_tweets = [str(t[1]) for t in ids]
	c = Counter(original_tweets)
	for pair in c.most_common(5):
		most_retweeted.append(pair[0])
	cnt = 0
	for t in ids:
		if str(t[1]) in most_retweeted and cnt < 500:
			graph.append({'source': str(t[0]), 'target': str(t[1]), 'group': most_retweeted.index(str(t[1]))})
			cnt += 1
	with open('json/retweets.json','w') as f:
		json.dump(graph,f)	
	