import time
import diary_tweet as dt

if __name__ == '__main__':
    diary_entry = dt.generate_diary_entry()
    dt.tweet(diary_entry)
    time.sleep(7200)
