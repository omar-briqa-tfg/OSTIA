from abc import ABC, abstractmethod


class IFilter(ABC):

    @abstractmethod
    def filter(cls, record: dict) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
