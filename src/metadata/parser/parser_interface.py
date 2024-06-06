from abc import ABC, abstractmethod


class IParser(ABC):

    @abstractmethod
    def parse(cls, metadata: dict) -> list[dict]:
        """
        Abstract method to parse a verbose metadata into a specific format.

        Subclasses must implement this method to provide specific parsing logic.

        :param metadata: The metadata entry to be parsed.
        :type metadata: dict
        :return: List of the metadata values parsed in the specified format.
        :rtype: list[dict]
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method")
