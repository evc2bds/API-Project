#Eloise Cunningham 10/20/21

import tweepy

consumer_key = "HjOY1Sw8Wjv3fXgeglI0LzszD"
consumer_secret_key = "P29b1zOQbecptwcZTreWeRXYve6tU1kB50MzJHVBkNN5HKZ3D8"
access_token = "1201310888499781632-JhSjVuuf2lYdIRqqChMq5h4UdsQv3k"
access_secret_token = "j8W7heIIxpVBdQ6r9MQU8TTdck5jsKWlzp944ZpKLOtI8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

account = api.get_user(screen_name="UVA")
#print UVA account details
print("Account Details: ")
print("   Name: " + account.screen_name)
print("   Follower Count: " + str(account.followers_count))
print()

#print the 3 most recent tweets from timeline and the time they were posted and who tweeted them
recent_tweets = api.home_timeline(count=3)
for tweet in recent_tweets:
    status = api.get_status(tweet.id)
    print("On " + str(status.created_at)[0:10] + " at" + str(status.created_at)[10:16] + " " + tweet.user.name + " tweeted:")
    print("   '" + tweet.text + "'")
    print()

#print the tweets that you have liked
print("You have liked the following tweets: ")
favorite_tweets = api.get_favorites()
for tweet in favorite_tweets:
    print("   " + tweet.user.screen_name + "'s tweet '" + str(tweet.text) + "'")
