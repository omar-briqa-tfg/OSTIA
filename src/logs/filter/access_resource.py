from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import BITSTREAM, HANDLE

import re


class AccessResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        return bool(re.search(HANDLE, resource)) or bool(re.search(BITSTREAM, resource))
