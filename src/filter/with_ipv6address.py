from src.filter.filter_interface import IFilter

from src.utils.regex_patterns import IPV6_PATTERN

import re


class WithIPv6Address(IFilter):

    @classmethod
    def filter(cls, log: str) -> bool:
        return bool(re.search(IPV6_PATTERN, log))
