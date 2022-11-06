"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""


from kedro.pipeline import Pipeline, node, pipeline

from company_social_media_feed.pipelines.data_processing.nodes import dummy_node



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
    data_processing = pipeline(
        pipe=pipeline_instance,
        inputs="company_data",
        namespace = "data_processing",
        outputs = "model_input_data"
    )
    return data_processing
