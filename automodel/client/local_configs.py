from enum import Enum

import os
import pathlib
import typing as tp
from pydantic import BaseModel


class LocalSettings(Enum):
    cache_folder='automodel'
    config_name = 'configs.yaml'
    cache_folder = '.cache'   


class BaseModel:
    def __init__(self):
        pass

class CacheMixin:
    def __init__(self):
        self.cache_folder = pathlib.Path.home() /  LocalSettings.cache_folder.value
        self.config_name =  LocalSettings.config_name
        self.config_path =  self.cache_folder / self.config_name.value
        self.configs = self.read_cache()
    def create_cache(self):
        self.cache_folder.mkdir(exist_ok=True)
    def update_cache(self):
        pass
    def read_cache(self):
        if self.config_path.exists():
            return  self.config_path.read_text()
        else:
            raise ValueError(
                'No config'
            )
    @classmethod
    def from_cache(cls):
        cls(
            LocalSettings
        )
        

class LocalConfig:
    def __init__(self,token:tp.Optional[str]):
        self.token = token
        
    @classmethod
    def from_environs(cls):
        return cls(
            token = os.environ.get('AUTOMODEL_TOKEN')
        )




        
