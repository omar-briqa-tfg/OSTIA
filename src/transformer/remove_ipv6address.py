from src.transformer.transformer_interface import ITransformer

import re

class RemoveIPv6Address(ITransformer):

    IPV6_PATTERN = r"^([a-fA-F0-9:]+|[uU]nknown), "

    @classmethod
    def transform(cls, log: str) -> str:

        while re.match(cls.IPV6_PATTERN, log):
            log = re.sub(cls.IPV6_PATTERN, "", log)

        return log
