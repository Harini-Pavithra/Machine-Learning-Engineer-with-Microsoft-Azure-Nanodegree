import json
import pandas as pd
import os
import joblib, pickle
from azureml.core import Model

def init():
    global daone
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'best-automl.pkl')
    #model_path = Model.get_model_path('best-automl.pkl')
    daone = joblib.load(model_path)

def run(data):
    try:
        trynn = json.loads(data)
        data = pd.DataFrame(trynn['data'])
        result = daone.predict(data)
        # You can return any data type, as long as it is JSON serializable.
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
