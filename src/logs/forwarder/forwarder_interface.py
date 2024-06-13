from abc import ABC, abstractmethod


class IForwarder(ABC):

    # TODO: replace int by Response class

    @abstractmethod
    def forward(cls, log: dict, raw_log: str) -> int:
        """
        Abstract method to define the log forwarding process.

        Subclasses must implement this method to provide specific support for specific storage solutions.

        :param log: The processed log entry to be forwarded, represented as a dictionary.
        :type log: dict
        :param raw_log: The log entry to be checked.
        :type raw_log: str
        :return: Status code of the log forwarding action.
        :rtype: int
        :raises NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method")
