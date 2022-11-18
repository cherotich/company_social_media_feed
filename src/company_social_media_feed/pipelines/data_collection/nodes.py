"""
This is a boilerplate pipeline 'data_collection'
generated using Kedro 0.18.3
"""
from typing import Dict
import numpy as np
import pandas as pd
from pyspark.sql import DataFrame
import snscrape.modules.twitter as sntwitter
from datetime import date


def fetch_all_tweets():
    ''' Fetch all tweets from 2017 september based on the keywords provided, it returns a dataframe'''
    tweets_list2 = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'(shell affordable energy) OR (shell clean energy) OR (shell affordable clean energy)  OR (shell decent work) OR (shell economic growth) OR (shell decent work economic growth) OR (shell industry innovation infrastructure) OR (shell innovation) OR (shell industry innovation) OR (shell responsible consumption) OR (shell responsible production) OR (shell climate action) OR (shell parternship) OR (shell partnership for goals)  lang:en since:2022-09-01 until:{date.today()}').get_items()):
        tweets_list2.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username,tweet.user.verified,tweet.user.location,tweet.replyCount,tweet.retweetCount,tweet.likeCount,tweet.quoteCount,tweet.url])
        df = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet_Id', 'Text', 'Username','Verified','Location','Reply_Count','Retweet_Count','Like_Count','Quote_Count','url'])
    return df


