"""
This is a boilerplate pipeline 'data_collection'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from company_social_media_feed.pipelines.data_collection.nodes import fetch_all_tweets




def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [

                node(
                func=fetch_all_tweets,
                inputs=None,
                outputs='raw_data',
                name= "twitter_data_collection_node",

            ),
        ]
    )
    data_collection = pipeline(
        pipe=pipeline_instance,
        inputs=None,
        namespace = "data_collection",
        outputs = "raw_data"

    )
    return data_collection

