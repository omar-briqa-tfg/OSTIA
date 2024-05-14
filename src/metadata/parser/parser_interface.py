from abc import ABC, abstractmethod


class IParser(ABC):

    @abstractmethod
    def parse(cls, metadata: dict) -> list[dict]:
        raise NotImplementedError("Subclasses must implement this method")
