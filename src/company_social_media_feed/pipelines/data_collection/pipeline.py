"""
This is a boilerplate pipeline 'data_collection'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

<<<<<<< HEAD
from company_social_media_feed.pipelines.data_collection.nodes import fetch_all_tweets
=======
from company_social_media_feed.pipelines.data_collection.nodes import dummy_node
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c



def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
<<<<<<< HEAD
                node(
                func=fetch_all_tweets,
                inputs=None,
                outputs='raw_data',
                name= "data_collection_node",
=======
            node(
                func=dummy_node,
                inputs="company_data",
                outputs="model_input_data",
                name="dummy_node",
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
            ),
        ]
    )
    data_collection = pipeline(
        pipe=pipeline_instance,
<<<<<<< HEAD
        inputs=None,
        namespace = "data_collection",
        outputs = "raw_data"
=======
        inputs="company_data",
        namespace = "data_collection",
        outputs = "model_input_data"
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
    )
    return data_collection

