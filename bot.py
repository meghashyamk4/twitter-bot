import tweepy
import time

auth = tweepy.OAuthHandler('xmQnE3aGsE60qwkMJVVnROppc', 'X2OLnsTOhPslSEMixqUIBGCOMrTobcy9R2VZpcgHETGu3kI31X')
auth.set_access_token('1159467000818569217-RH7f7b7YVg1sqjqElUteq1m7TcyPvM', 'zUIdzI5A9IYSecn7dN6jZEkTgL7l17X15DeWCjNIdFDYD')
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name) :
	f_read = open(file_name,'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name) :
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()

def reply_to_tweets() :
	print("Replying to new tweets.... ")
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
	for i in reversed(mentions) :
		print(str(i.id) + " " + i.full_text)
		last_seen_id = i.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if '#helloworld' in i.full_text.lower() :
			print("Tweet with HashTag #helloworld found !!")
			print("....now replying to that tweet.....")
			api.update_status('@' + i.user.screen_name + ' Heyy, ' + i.user.name + ' #Hello_!!', i.id)

while True :
	reply_to_tweets()
	time.sleep(10)
			
