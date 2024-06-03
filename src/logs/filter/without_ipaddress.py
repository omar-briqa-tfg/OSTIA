from src.logs.filter.filter_interface import IFilter


class WithoutIpAddress(IFilter):

    WITHOUT_IPADDRESS = '-'

    @classmethod
    def filter(cls, log: str) -> bool:
        """
        Checks if the given log entry does not contain an IP address.

        :param log: The log entry to be checked.
        :type log: str
        :return: True if the first character of the log entry matches ``WITHOUT_IPADDRESS``, False otherwise.
        :rtype: bool
        """
        return log[0] == cls.WITHOUT_IPADDRESS
