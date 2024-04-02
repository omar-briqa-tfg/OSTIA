from src.log import Log

from typing import List

from abc import ABC, abstractmethod

class IForwarder(ABC):

    #TODO: replace int by Response class

    @abstractmethod
    def forward(self, log: Log) -> int:
        pass

    @abstractmethod
    def forwardMany(self, logs: List[Log]) -> int:
        pass
