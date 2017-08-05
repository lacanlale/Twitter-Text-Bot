#!/usr/bin/python
import tweepy
from auth_keys import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

def text_tweet():
    text = next_text()
    api.update_status(text)
    increment_file(current_index())

def next_text():
    num = current_index()
    with open('/Users/admin/datebot/tweets.txt', "r") as file:
	for line in range(num+1):
		path = file.readline().strip()
	print(path)
	return path

def increment_file(num):
	with open('/Users/admin/datebot/tweet_index.txt', "w") as file:
		file.truncate()
		file.write('%d' % (num+1))
		file.close

def current_index():
	with open('/Users/admin/datebot/tweet_index.txt', "r") as file:
		num = file.readline().strip()
	file.close()
	return int(num)

text_tweet()
