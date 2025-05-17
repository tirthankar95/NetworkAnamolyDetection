from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from model_code.model import BaseModel, DATA, MAPPING
import pandas as pd 
import pickle 
from pathlib import Path

class SVCModel(BaseModel):
    def __init__(self):
        self.dpath = DATA
        with open(self.dpath, "rb") as f:
            self.data = pickle.load(f)
        with open(MAPPING, "rb") as f:
            self.mapping = pickle.load(f)
        self.helper_dir = Path(self.dpath).parent 
        self.rmap = {v: k for k, v in self.mapping['attack'].items()}
        self.target_names = [self.rmap[i] for i in range(len(self.rmap))]
        # Get default values for each column.
        with open(self.helper_dir / "default_values.pkl", "rb") as f:
            self.default_values = pickle.load(f)
        del self.default_values['attack']
        # Get scaler.
        with open(self.helper_dir / "scaler.pkl", "rb") as f:
            self.scaler = pickle.load(f)
        

    def is_numeric(self, x):
        if type(x) == int or type(x) == float:
            return True
        return False 
    
    def train(self):
        if not Path(self.helper_dir / "svc.pkl").exists():
            '''
            These parameters are for OneVsRestClassifier.
            estimator__C is Inv of regularization strength.
            '''
            parameters = {
                'estimator__C': [1.0, 0.1],
                'estimator__kernel': ['linear', 'rbf']
            }
            model = OneVsRestClassifier(SVC())
            clf = GridSearchCV(model, parameters, cv=3)
            clf.fit(pd.concat([self.data["X_tr"], self.data["X_cv"]]), 
                    pd.concat([self.data["Y_tr"], self.data["Y_cv"]]))
            self.model = clf.best_estimator_ 
            self.model.fit(self.data["X_tr"], self.data["Y_tr"])
            # SAVE MODEL 
            with open(self.helper_dir / "svc.pkl", "wb") as f:
                pickle.dump(self.model, f)
        # LOAD MODEL 
        with open(self.helper_dir / "svc.pkl", "rb") as f:
            self.model = pickle.load(f)
        # GET PREDICTIONS ON CV 
        yp = self.model.predict(self.data["X_cv"])
        cv_report = classification_report(self.data["Y_cv"], yp, 
                                          target_names = self.target_names)
        yp = self.model.predict(self.data["X_test"])
        test_report = classification_report(self.data["Y_test"], yp, 
                                            target_names = self.target_names)
        return {"cv_report": cv_report, "test_report": test_report}
    
    def predict(self, nw_data):
        nw_data = nw_data.dict()
        if nw_data is None:
            return ['No data to make prediction.']
        if not Path(self.helper_dir / "svc.pkl").exists():
            return ['Model not ready yet.']
        with open(self.helper_dir / "svc.pkl", "rb") as f:
            self.model = pickle.load(f)
        X_test = {}
        # Re-arrange the data. 
        features = self.data['X_tr'].columns
        for cols, val in nw_data.items():
            if cols not in features:
                print(f'{cols}: bad column')
            if cols not in features or \
            (not self.is_numeric(val) and \
             cols not in self.mapping[cols]):
                X_test[cols] = [self.default_values[cols]]
            else:
                X_test[cols] = [val]
        X_test = pd.DataFrame(X_test)
        orig_columns = X_test.columns
        X_test = self.scaler.transform(X_test)
        X_test = pd.DataFrame(X_test, columns = orig_columns)
        # Make prediction
        yp = self.model.predict(X_test)
        return [self.rmap[y] for y in yp]