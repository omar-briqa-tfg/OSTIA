from src.log import Log

from abc import ABC, abstractmethod

class ITransformer(ABC):

    @abstractmethod
    def transform(self, log: Log) -> Log:
        pass
