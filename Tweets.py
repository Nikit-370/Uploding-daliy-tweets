import random
from random_words import RandomWords
from PyDictionary import PyDictionary
import tweepy
import datetime
import time

consumer_key = "cV5RlGN3BooV2sQePxQzfUc0d"
consumer_secret_key = "WTL9inZFcXN9n8059aiYs9bdgCbv5WrK6Hf0eaPyazizmK8TrH"

access_token = "1221634186970390528-rldPYyxW4D7rW7FpjLqvV4FDZEsDMg"
access_token_secret = "McNeg4d4UD2QjzQoLTJ2ITfrKN33VC2jkiH5IBzhhShb8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def loadRandomWord():
    dictionary = PyDictionary()
    rw = RandomWords()

    word = rw.random_word()
    definitions = dictionary.meaning(word)

    try:
        part_of_speech = random.choice( list ( definitions.keys() ) )
        definition = random.choice( definitions[part_of_speech] )
    except:
        return "NULL_DEFINITION"
    
    return {
        "word": word,
        "definition": definition,
        "part_of_speech": part_of_speech
    }

while (True):
    if (datetime.datetime.now().hour >= 8 and datetime.datetime.now().hour <= 10):
        word_of_the_day = loadRandomWord()

        while (word_of_the_day == "NULL_DEFINITION"):
            word_of_the_day = loadRandomWord()

        wotd_tweet = f'Today\'s #WordOfTheDay is \'{word_of_the_day["word"]}\'.  It means \'{word_of_the_day["definition"]}\' as a {word_of_the_day["part_of_speech"]}.'

        api.update_with_media("name_of_your_file", wotd_tweet) #Replace 'name of the file' you want to upload or you can give location too
    
    time.sleep(1.75 * 3600) # 1hr 45min