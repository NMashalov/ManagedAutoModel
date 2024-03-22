import requests
import s3fs
from dataclasses import dataclass

@dataclass
class S3configs:
    key: str
    secret: str
    endpoint_url: str

class s3UploadMixin:
    def __init__(self,configs):
        self.s3_client = s3fs.S3FileSystem(
            key=S3configs.key,
            secret=S3configs.secret,
            endpoint_url=S3configs.endpoint_url
        )

    @classmethod    
    def recieve_by_token(cls, token):
        requests.get(data={'token':'token'})

    def push_to_hub(self):
        pass


@dataclass
class Httpconfigs:
    url: str


class HttpUploadMixin:
    def __init__(self,configs:  Httpconfigs):
        self.url = self.url

    def push_to_hub(self,data):
        requests.post(
            self.url,
            data=data
        )
