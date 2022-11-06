"""
This is a boilerplate pipeline 'data_collection'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline

from company_social_media_feed.pipelines.data_collection.nodes import dummy_node



def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(
                func=dummy_node,
                inputs="company_data",
                outputs="model_input_data",
                name="dummy_node",
            ),
        ]
    )
    data_collection = pipeline(
        pipe=pipeline_instance,
        inputs="company_data",
        namespace = "data_collection",
        outputs = "model_input_data"
    )
    return data_collection

