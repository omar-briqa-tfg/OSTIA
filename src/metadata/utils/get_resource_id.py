from src.metadata.utils.regex_patterns import HANDLE

import re


def get_resource_id(resource_identifier: str) -> str:
    return re.compile(HANDLE).findall(resource_identifier)[0][0]
