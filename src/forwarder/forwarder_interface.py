from abc import ABC, abstractmethod

class IForwarder(ABC):

    #TODO: replace int by Response class

    @abstractmethod
    def forward(self, log: str) -> int:
        pass
