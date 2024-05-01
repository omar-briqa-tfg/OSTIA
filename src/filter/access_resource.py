from src.filter.filter_interface import IFilter

from src.utils.regex_patterns import BITSTREAM, HANDLE

import re

class AccessResource(IFilter):

    @classmethod
    def filter(cls, log: str) -> bool:
        return bool(re.search(HANDLE, log)) or bool(re.search(BITSTREAM, log))
