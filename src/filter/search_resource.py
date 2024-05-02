from src.filter.filter_interface import IFilter

class SearchResource(IFilter):

    #TODO: complete list
    SEARCH_KEYS = ['discover?', 'search?', 'browse?', 'open-search?']

    @classmethod
    def filter(cls, resource: str) -> bool:
        return any(key in resource for key in cls.SEARCH_KEYS)
