import os
import sys
from .exception import CustomException
from .logger import logging
import pandas as pd

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