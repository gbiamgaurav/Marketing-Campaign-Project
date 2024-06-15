
from Prediction_project import logger
from Prediction_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Prediction_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    raise e