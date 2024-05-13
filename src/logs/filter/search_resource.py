from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import SEARCH_KEYS


class SearchResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        return any(key in resource for key in SEARCH_KEYS)
