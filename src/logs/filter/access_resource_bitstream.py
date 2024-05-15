from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import BITSTREAM

import re


class AccessResourceBitstream(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        return bool(re.search(BITSTREAM, resource))
