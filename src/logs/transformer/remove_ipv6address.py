from src.logs.transformer.transformer_interface import ITransformer

from src.logs.utils.regex_patterns import IPV6_PATTERN

import re


class RemoveIPv6Address(ITransformer):

    @classmethod
    def transform(cls, log: str) -> str:
        """
        Removes every IPv6 occurrence from the **log**.

        :param log: Log entry to be transformed.
        :type log: str
        :return: The log where every ``IPV6_PATTERN`` has been replaced by an empty string.
        :rtype: str
        """
        while re.match(IPV6_PATTERN, log):
            log = re.sub(IPV6_PATTERN, "", log)

        return log
