"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""


from kedro.pipeline import Pipeline, node, pipeline

<<<<<<< HEAD
from company_social_media_feed.pipelines.data_processing.nodes import preprocess_data
=======
from company_social_media_feed.pipelines.data_processing.nodes import dummy_node
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c



def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(
<<<<<<< HEAD
                func=preprocess_data,
                inputs="raw_data",
                outputs="cleaned_data",
                name="data_preprocessing_node",
=======
                func=dummy_node,
                inputs="company_data",
                outputs="model_input_data",
                name="dummy_node",
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
            ),
        ]
    )
    data_processing = pipeline(
        pipe=pipeline_instance,
<<<<<<< HEAD
        inputs="raw_data",
        namespace = "data_processing",
        outputs = "cleaned_data"
=======
        inputs="company_data",
        namespace = "data_processing",
        outputs = "model_input_data"
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
    )
    return data_processing
