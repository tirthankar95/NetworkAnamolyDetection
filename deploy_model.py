from typing import Union, Optional
from model_code.LogisiticRegression import LRModel
from pydantic import BaseModel 
from fastapi import (
    FastAPI
)

class NetworkItem(BaseModel):
    duration: Optional[float] = None
    protocoltype: Optional[str] = None 
    service: Optional[str] = None       
    flag: Optional[str] = None
    srcbytes: Optional[float] = None
    dstbytes: Optional[float] = None
    land: Optional[float] = None
    wrongfragment: Optional[float] = None
    urgent: Optional[float] = None
    hot: Optional[float] = None
    numfailedlogins: Optional[float] = None
    loggedin: Optional[float] = None
    numcompromised: Optional[float] = None
    rootshell: Optional[float] = None
    suattempted: Optional[float] = None
    numroot: Optional[float] = None
    numfilecreations: Optional[float] = None
    numshells: Optional[float] = None
    numaccessfiles: Optional[float] = None
    numoutboundcmds: Optional[float] = None
    ishostlogin: Optional[float] = None
    isguestlogin: Optional[float] = None
    count: Optional[float] = None
    srvcount: Optional[float] = None
    serrorrate: Optional[float] = None
    srvserrorrate: Optional[float] = None
    rerrorrate: Optional[float] = None
    srvrerrorrate: Optional[float] = None
    samesrvrate: Optional[float] = None
    diffsrvrate: Optional[float] = None
    srvdiffhostrate: Optional[float] = None
    dsthostcount: Optional[float] = None
    dsthostsrvcount: Optional[float] = None
    dsthostsamesrvrate: Optional[float] = None
    dsthostdiffsrvrate: Optional[float] = None
    dsthostsamesrcportrate: Optional[float] = None
    dsthostsrvdiffhostrate: Optional[float] = None
    dsthostserrorrate: Optional[float] = None
    dsthostsrvserrorrate: Optional[float] = None
    dsthostrerrorrate: Optional[float] = None
    dsthostsrvrerrorrate: Optional[float] = None
    lastflag: Optional[float] = None

app = FastAPI()
# Logistic Regression Model
obj_lr = LRModel()
obj_lr.train() # This model is trained only once, so no time is consumed.

@app.post("/predict")
def predict(NetworkItem: Union[NetworkItem, None]):
    res = {}
    res['Logistic Reg. attack_type'] = obj_lr.predict(NetworkItem)
    return res