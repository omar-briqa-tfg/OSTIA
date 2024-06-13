from abc import ABC, abstractmethod


class IFilter(ABC):

    @abstractmethod
    def filter(cls, log: str) -> bool:
        """
        Abstract method to determine if a given log entry matches certain criteria.

        Subclasses must implement this method to provide specific filtering logic.

        :param log: The log entry to be checked.
        :type log: str
        :return: True if the log entry matches the criteria, False otherwise.
        :rtype: bool
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method")
