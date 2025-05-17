from abc import ABC, abstractmethod
from pathlib import Path

DATA = Path(__file__).parent.parent / "data_and_models" / "dataset.pkl"
DATA_TREE = Path(__file__).parent.parent / "data_and_models" / "dataset_tree.pkl"
MAPPING = Path(__file__).parent.parent / "data_and_models" / "mapping.pkl"

class BaseModel(ABC):
    @abstractmethod
    def train(self):
        pass 
    @abstractmethod
    def predict(self, newtork_data):
        pass