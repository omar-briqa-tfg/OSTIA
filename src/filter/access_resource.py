from src.filter.filter_interface import IFilter

import re

class AccessResource(IFilter):

    HANDLE_BITSTREAM = r'((2099(.[1-4])?|2117)\/\d+)|bitstream\/id\/([^\/]*)\/'

    @classmethod
    def filter(self, log: str) -> bool:
        return bool(re.search(self.HANDLE_BITSTREAM, log))
