from ..local_configs import LocalConfig
from catboost import CatBoostClassifier
from pathlib import Path

class CatboostAutoModel:
    def __init__(self,model: CatBoostClassifier, features: list[str]):
        self.model = model
        self.feature_list = features
    

    

    @classmethod
    def from_pretrained(self,conifg_name:str| Path):
        '''
        Can be provided
        '''
        pass

