from src.log import Log

from typing import Dict, Any

from abc import ABC, abstractmethod

class IFilter(ABC):

    @abstractmethod
    def filter(self, log: Log) -> bool:
        pass

    @abstractmethod
    def get_parameters(self) -> Dict[str, Any]:
        pass