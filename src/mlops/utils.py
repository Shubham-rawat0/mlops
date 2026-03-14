import os
import sys
from .exception import CustomException
from .logger import logging
import pandas as pd
import pickle

def read_csv_data():
    file_path = os.path.join("notebook", "data", "raw.csv")
    logging.info("Reading CSV file started")
    try:
        df = pd.read_csv(file_path)
        logging.info("CSV loaded successfully")
        print(df.head())
        return df

    except Exception as e:
        raise CustomException(e, sys)
    
def save_objects(file_path , obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)