from abc import ABC, abstractmethod


class IForwarder(ABC):

    # TODO: replace int by Response class

    @abstractmethod
    def forward(cls, log: dict, raw_log: str) -> int:
        pass
