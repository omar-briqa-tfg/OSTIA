from src.filter.filter_interface import IFilter

class SearchResource(IFilter):

    #TODO: complete list
    SEARCH_KEYS = ['discover', 'search', 'browse', 'open-search']

    @classmethod
    def filter(cls, log: str) -> bool:
        return any(key in log for key in cls.SEARCH_KEYS)
