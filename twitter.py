import tweepy

# Remplace ces valeurs par tes clés API
BEARER_TOKEN = "ton_bearer_token"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Recherche des tweets contenant un mot-clé
query = "Python -is:retweet lang:fr"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)