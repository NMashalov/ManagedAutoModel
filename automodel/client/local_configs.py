from enum import Enum
import s3fs
import os
import pathlib
import typing as tp
     
class LocalSettings(Enum):
    cache_folder='automodel'
    config_name = 'configs.yaml'
    cache_folder = '.cache'        

class LocalConfig:

    def __init__(self,token:tp.Optional[str]):
        self.token = token
        self.config_path = pathlib.Path.home() / self.cache_folder / self.config_name.value

    @classmethod
    def from_environs(cls):
        return cls(
            token = os.environ.get('AUTOMODEL_TOKEN')
        )

    def create_cache(self):
        config_path

    def update_cache(self):
        config_folder = pathlib.Path.home() / '.cache'

    def to_cache(self):
        LocalSettings.cache_folder.value

    def from_cache(self):
        LocalSettings
        if cache_folder.exist():
            cache_folder.mkdir()

    @classmethod
    def from_cache():



        
