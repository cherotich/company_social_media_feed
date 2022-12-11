"""
This is a boilerplate pipeline 'data_collection'
generated using Kedro 0.18.3
"""
from typing import Dict
import pandas as pd
import snscrape.modules.twitter as sntwitter
from datetime import date


def fetch_all_tweets(company_name,start_year,end_year):
    ''' Fetch all tweets from 2017 september based on the keywords provided, it returns a dataframe'''
    tweets_list2 = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'({company_name} affordable energy) OR ({company_name} clean energy) OR ({company_name} affordable clean energy)  OR ({company_name} decent work) OR ({company_name} economic growth) OR ({company_name} decent work economic growth) OR ({company_name} industry innovation infrastructure) OR ({company_name} innovation) OR ({company_name} industry innovation) OR ({company_name} responsible consumption) OR ({company_name} responsible production) OR ({company_name} climate action) OR ({company_name} parternship) OR ({company_name} partnership for goals)  lang:en since:{start_year}-01-01 until:{end_year}-12-31').get_items()):
        tweets_list2.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username,tweet.user.verified,tweet.user.location,tweet.replyCount,tweet.retweetCount,tweet.likeCount,tweet.quoteCount,tweet.url])
        df = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet_Id', 'Text', 'Username','Verified','Location','Reply_Count','Retweet_Count','Like_Count','Quote_Count','url'])
    return df




