"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
import pandas as pd
import re
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

def _clean_tweet(tweet):
    '''
    tweet: String
           Input Data
    tweet: String
           Output Data
           
    func: Removes hashtag symbol in front of a word
          Replace URLs with a space in the message
          Replace ticker symbols with space. The ticker symbols are any stock symbol that starts with $.
          Replace  usernames with space. The usernames are any word that starts with @.
          Replace everything not a letter or apostrophe with space
          Remove single letter words
          filter all the non-alphabetic words, then join them again
    '''
    
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = re.sub('\$[a-zA-Z0-9]*', ' ', tweet)
    tweet = re.sub('\@[a-zA-Z0-9]*', ' ', tweet)
    tweet = re.sub('[^a-zA-Z\']', ' ', tweet)
    tweet = re.sub(r'\s+', " ", tweet)
    tweet = ' '.join( [w for w in tweet.split() if len(w)>1] )
    
    return tweet

# def _split_date(date):


def _token_stop_pos(text):
        '''
        Maps the part of speech to words in sentences giving consideration to words that are nouns, verbs, 
        adjectives and adverbs
        '''
        pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
        tags = pos_tag(word_tokenize(text))
        newlist = []
        for word, tag in tags:
            if word.lower() not in set(stopwords.words('english')):
                newlist.append(tuple([word, pos_dict.get(tag[0])]))
        return newlist


def _lemmatize_tweets(text: str) -> str:
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    #text = text.lower() text the moment is a list and not a string - something is wrong here
    text = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
    return ' '.join(text)

def preprocess_data(df)->pd.DataFrame:
    '''
    Function takes in the whole dataframe and carries out the following preprocessing steps:
    1. General text cleaning
    2. Part of Speech tagging
    3. Lemmatization
    Then return the dataframe
    ''' 
    df['clean_text'] = df['Text'].apply(lambda x:_clean_tweet(x))
    df['POS tagged'] = df['clean_text'].apply(_token_stop_pos)
    df['Lemma'] = df['clean_text'].apply(_lemmatize_tweets)
    df['hashtags'] = df['Text'].apply(lambda x: " ".join ([w for w in x.split() if '#'  in w[0:3] ]))
    df['hashtags']=df['hashtags'].str.replace("[^a-zA-Z0–9]", ' ')
    df = df.loc[:,['Datetime', 'Tweet_Id','Username','Verified','Location','Reply_Count','Retweet_Count','Like_Count','Quote_Count','url','clean_text','hashtags','POS tagged','Lemma']]

    return df
