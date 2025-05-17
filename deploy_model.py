from typing import Union
from model_code.LogisiticRegression import LRModel
from pydantic import BaseModel 
from fastapi import (
    FastAPI
)

class NetworkItem(BaseModel):
    duration: int 
    protocol_type: str 
    service: str 
    flag: str 
    srcbytes: int 
    dstbytes: int
    land: int
    wrongfragment: int 
    urgent: int
    hot: int

app = FastAPI()
# Logistic Regression Model
obj_lr = LRModel()
obj_lr.train() # This model is trained only once, so no time is consumed.

@app.post("/predict")
def predict(NetworkItem: Union[NetworkItem, None]):
    res = {}
    res['Logistic Reg. attack_type'] = obj_lr.predict(NetworkItem)
    return res