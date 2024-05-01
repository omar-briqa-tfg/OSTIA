from src.filter.filter_interface import IFilter

import re

class WebResource(IFilter):

    WEB_EXTENSIONS = r'.*\.(js|woff|jpg|css|png(.*)?|ico|txt|gif)$'

    @classmethod
    def filter(cls, log: str) -> bool:
        return bool(re.search(cls.WEB_EXTENSIONS, log))
