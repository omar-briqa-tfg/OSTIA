from src.filter.filter_interface import IFilter

from src.utils.regex_patterns import WEB_EXTENSIONS

import re

class WebResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        return bool(re.search(WEB_EXTENSIONS, resource))
