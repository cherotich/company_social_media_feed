"""
This is a boilerplate pipeline 'data_analytics'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

<<<<<<< HEAD
from company_social_media_feed.pipelines.data_analytics.nodes import label_tweet
=======
from company_social_media_feed.pipelines.data_analytics.nodes import dummy_node
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c



def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(
<<<<<<< HEAD
                func=label_tweet,
                inputs="cleaned_data",
                outputs="labelled_data",
                name="data_analytics_node",
=======
                func=dummy_node,
                inputs="company_data",
                outputs="model_input_data",
                name="dummy_node",
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
            ),
        ]
    )
    data_analytics = pipeline(
        pipe=pipeline_instance,
<<<<<<< HEAD
        inputs="cleaned_data",
        namespace = "data_analytics",
        outputs = 'labelled_data'
=======
        inputs="company_data",
        namespace = "data_analytics",
        outputs = "model_input_data"
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
    )
    return data_analytics
