"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""


from kedro.pipeline import Pipeline, node, pipeline

from company_social_media_feed.pipelines.data_processing.nodes import preprocess_data



def create_pipeline(**kwargs) -> Pipeline:
    pipeline_instance =  pipeline(
        
        [
            node(
                func=preprocess_data,
                inputs="raw_data",
                outputs="cleaned_data",
                name="data_preprocessing_node",
            ),
        ]
    )
    data_processing = pipeline(
        pipe=pipeline_instance,
        inputs="raw_data",
        namespace = "data_processing",
        outputs = "cleaned_data"
    )
    return data_processing
