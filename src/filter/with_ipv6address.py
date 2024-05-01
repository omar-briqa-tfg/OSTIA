from src.filter.filter_interface import IFilter

import re

class WithIPv6Address(IFilter):

    IPV6_PATTERN = r"^([a-fA-F0-9:]+|[uU]nknown), "

    @classmethod
    def filter(cls, log: str) -> bool:
        return bool(re.search(cls.IPV6_PATTERN, log))
