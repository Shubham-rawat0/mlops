import sys
sys.path.insert(0, '.')

from src.mlops.logger import logging
from src.mlops.exception import CustomException

from src.mlops.components.data_ingestion import DataIngestion
from src.mlops.components.data_transformation import DataTransformationConfig
from src.mlops.components.data_transformation import DataTransformation

if __name__ == "__main__":
    logging.info("The app has started")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    except Exception as e:
        raise CustomException(e,sys) 

