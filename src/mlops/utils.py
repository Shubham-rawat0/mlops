import os
import sys
from .exception import CustomException
from .logger import logging
import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        best_params = {}
        for name, model in models.items():

            para = param[name]

            gs = GridSearchCV(model, para, cv=3,verbose=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            test_score = r2_score(y_test, y_test_pred)

            report[name] = test_score
            best_params[name] = gs.best_params_
            
        return report, best_params

    except Exception as e:
        raise CustomException(e, sys)