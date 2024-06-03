from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import SEARCH_KEYS


class SearchResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        """
        Determines if the given **resource** is a search in UPCommons.

        :param resource: The resource string to be checked.
        :type resource: str
        :return: True if the resource search key is in the ``SEARCH_KEYS`` list, False otherwise.
        :rtype: bool
        """
        return any(key in resource for key in SEARCH_KEYS)
