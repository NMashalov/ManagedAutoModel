import abc
import s3fs

class AbstractModelConfig(abc.ABC):
    pass


class AbstractModel:

    @classmethod
    def from_configs(cls,model_name:str):
        cls(
            model_name
        )

    @abc.abstractmethod
    def storage_format():
        pass
    
    @abc.abstractmethod
    def push_to_hub(self):
        pass

    @abc.abstractmethod
    def serve(self):
        pass

    @abc.abstractmethod
    def schedule(self):
        pass

    