"""
This is a boilerplate pipeline 'data_analytics'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from company_social_media_feed.pipelines.data_analytics.nodes import label_tweet




def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(

                func=label_tweet,
                inputs="cleaned_data",
                outputs="labelled_data",
                name="data_analytics_node",

            ),
            
        ]
    )
    data_analytics = pipeline(
        pipe=pipeline_instance,
        inputs="cleaned_data",
        namespace = "data_analytics",
        outputs = 'labelled_data'

    )
    return data_analytics
