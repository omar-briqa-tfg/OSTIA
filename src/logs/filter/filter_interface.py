from abc import ABC, abstractmethod


class IFilter(ABC):

    @abstractmethod
    def filter(cls, log: str) -> bool:
        pass
