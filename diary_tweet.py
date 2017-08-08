import time
import markovify
import tweepy
import private

file_path = "file"
# Twitter Markov Bot
def generate_model(file_path):
    '''read in .txt file, build markov model'''
    # Get raw text as string.
    with open(file_path) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)

    return text_model

text_model = generate_model(file_path)

def tweet(n):
    '''create tweet and send to the interent for everyone to see'''
    diary_entry = text_model.make_short_sentence(140)

    auth = tweepy.OAuthHandler(private.CONSUMER_KEY,
                               private.CONSUMER_SECRET)  # (CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(private.ACCESS_TOKEN,
                          private.ACCESS_SECRET)  # (ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api.update_status(diary_entry)
