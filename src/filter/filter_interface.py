from abc import ABC, abstractmethod

class IFilter(ABC):

    @abstractmethod
    def filter(self, log: str) -> bool:
        pass
