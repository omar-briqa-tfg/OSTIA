from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import HANDLE

import re


class AccessResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        """
        Determines if the given **resource** is an access resource to UPCommons via a *handle*.

        :param resource: The resource string to be checked.
        :type resource: str
        :return: True if the resource matches the ``HANDLE`` pattern, False otherwise.
        :rtype: bool
        """
        return bool(re.search(HANDLE, resource))
