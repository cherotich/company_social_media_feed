"""Project pipelines."""
from typing import Dict

<<<<<<< HEAD
=======
from kedro.framework.project import find_pipelines
>>>>>>> 136b2c5d3f082e71849c746b59257576b6b1e43c
from kedro.pipeline import Pipeline
from company_social_media_feed.pipelines import data_collection as dc
from company_social_media_feed.pipelines import data_processing as dp
from company_social_media_feed.pipelines import data_analytics as da

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_collection = dc.create_pipeline()
    data_processing = dp.create_pipeline()
    data_analytics = da.create_pipeline()
    return {"__default__": data_collection+data_processing+data_analytics,
            "data_collection": data_collection,   
            "data_processing":data_processing,
            "data_analytics":data_analytics  

    }
