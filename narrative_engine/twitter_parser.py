# narrative_engine/twitter_parser.py

import tweepy

class TwitterSentiment:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token)

    def search_tweets(self, query, max_results=10):
        tweets = self.client.search_recent_tweets(query=query, max_results=max_results)
        return [tweet.text for tweet in tweets.data]

if __name__ == "__main__":
    BEARER_TOKEN = "INSERT_YOUR_TWITTER_BEARER_TOKEN"
    ts = TwitterSentiment(BEARER_TOKEN)
    tweets = ts.search_tweets("bitcoin")
    print(tweets)
