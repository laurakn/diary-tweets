import time
import markovify
import tweepy
import private

file_path = "file"
# Twitter Markov Bot
def generate_diary_entry():
    '''read in .txt file, build markov model'''
    # Get raw text as string.
    with open(file_path) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)
    diary_entry = text_model.make_short_sentence(140)

    hashtag = "#teenageagnst"

    diary_entry = diary_entry + hashtag

    return diary_entry



def tweet():
    '''create tweet and send to the interent for everyone to see'''

    auth = tweepy.OAuthHandler(private.CONSUMER_KEY,
                               private.CONSUMER_SECRET)  # (CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(private.ACCESS_TOKEN,
                          private.ACCESS_SECRET)  # (ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api.update_status(diary_entry)
