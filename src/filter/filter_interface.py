from src.log import Log

from abc import ABC, abstractmethod

class IFilter(ABC):

    @abstractmethod
    def filter(self, log: Log) -> bool:
        pass
