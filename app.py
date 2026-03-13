import sys
sys.path.insert(0, '.')

from src.mlops.logger import logging
from src.mlops.exception import CustomException
from src.mlops.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info("The app has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys) 

