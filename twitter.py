import tweepy

# Remplace ces valeurs par tes clés API
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFXX0AEAAAAAp0Pg%2BCJEin979hFJS0injbEgLho%3DoA61Pc3bsfKgFNnpU1gpVBzBqDi0Di1Cx0hAd2csM180OxhVcs"

# Authentification avec l'API Twitter
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Recherche des tweets contenant un mot-clé
query = "data science -is:retweet lang:fr"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)