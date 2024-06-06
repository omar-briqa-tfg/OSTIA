from src.logs.filter.filter_interface import IFilter

from src.logs.utils.regex_patterns import WEB_EXTENSIONS

import re


class WebResource(IFilter):

    @classmethod
    def filter(cls, resource: str) -> bool:
        """
        Determines if the given **resource** is access to a web resource.

        :param resource: The resource string to be checked.
        :type resource: str
        :return: True if the resource matches the ``WEB_EXTENSIONS`` pattern, False otherwise.
        :rtype: bool
        """
        return bool(re.search(WEB_EXTENSIONS, resource))
