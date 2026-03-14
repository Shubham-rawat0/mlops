import sys
sys.path.insert(0, '.')

from src.mlops.logger import logging
from src.mlops.exception import CustomException

from src.mlops.components.data_ingestion import DataIngestion
from src.mlops.components.data_transformation import DataTransformation
from src.mlops.components.model_tranier import ModelTrainer

if __name__ == "__main__":
    logging.info("The app has started")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        train_arr, test_arr,patho = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        


    except Exception as e:
        raise CustomException(e,sys) 

