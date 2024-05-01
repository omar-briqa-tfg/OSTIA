from src.transformer.transformer_interface import ITransformer

from src.utils.regex_patterns import IPV6_PATTERN

import re

class RemoveIPv6Address(ITransformer):

    @classmethod
    def transform(cls, log: str) -> str:

        while re.match(IPV6_PATTERN, log):
            log = re.sub(IPV6_PATTERN, "", log)

        return log
