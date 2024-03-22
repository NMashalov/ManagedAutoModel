import abc

from dataclasses import dataclass


class AbstractModelConfig(abc.ABC):
    pass

class ReceievedModel:

    @classmethod
    def from_configs(cls,model_name:str):
        cls(
            model_name
        )

    @abc.abstractmethod
    def storage_format():
        pass

    @abc.abstractmethod
    def serve(self):
        pass

    @abc.abstractmethod
    def schedule(self):
        pass

    