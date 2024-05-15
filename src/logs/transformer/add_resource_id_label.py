from src.logs.transformer.transformer_interface import ITransformer

from src.logs.utils.regex_patterns import HANDLE

import re


class AddResourceIdLabel(ITransformer):

    @classmethod
    def transform(cls, log: dict, resource: str) -> None:

        handle = re.compile(HANDLE).findall(resource)
        if len(handle) > 0:

            ids = list({id[0] for id in handle})
            ids = ids[0] if len(ids) == 1 else ids

            log['resource'] = ids
