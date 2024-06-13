from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import IPV6_PATTERN

import re


class WithIPv6Address(IFilter):

    @classmethod
    def filter(cls, log: str) -> bool:
        """
        Checks if the given log entry contains an IPv6 address.

        :param log: The log entry to be checked.
        :type log: str
        :return: True if the log entry matches the ``IPV6_PATTERN`` pattern, False otherwise.
        :rtype: bool
        """
        return bool(re.search(IPV6_PATTERN, log))
