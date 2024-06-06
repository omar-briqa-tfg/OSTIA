from abc import ABC, abstractmethod


class IFilter(ABC):

    @abstractmethod
    def filter(cls, record: dict) -> bool:
        """
        Abstract method to determine if a given metadata entry matches certain criteria.

        Subclasses must implement this method to provide specific filtering logic.

        :param record: The record entry to be checked.
        :type record: dict
        :return: True if the metadata entry matches the criteria, False otherwise.
        :rtype: bool
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method")
