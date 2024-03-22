from enum import Enum
import typing as tp
import s3fs

class S3StorageConfigs(Enum):
    s3_bucket = 'models'
    max_version = 3 


class S3Manager:
    def __init__(self,
            token: tp.Optional[str]):
        '''
        Token allows
        '''
        self.s3_client = s3fs.S3FileSystem(
            key='miniokey...',
            secret='asecretkey...',
            endpoint_url='https://...'
        )

        self.bucket = S3StorageConfigs.s3_bucket
        
    @classmethod
    def register_from_cache(self):
        S3Model.cache_path.value 
        
        
    def upload_model() 
        fo = self.s3_client.open('versioned_bucket/object')


    @staticmethod
    def register(cls):


class DataModelConfigs:
    def __init__(self, s3_base_folder: str = 'models',  cache_name: str = 'automodel'):
        s3_bucket

    def push_to_hub(self):