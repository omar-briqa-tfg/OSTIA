from src.logs.transformer.transformer_interface import ITransformer

import re


class AddTimestamp(ITransformer):

    @classmethod
    def transform(cls, log: str, raw_log) -> None:
        log['date'] = re.compile(r'\d{1,2}/\w{3}/\d{1,4}').findall(raw_log)[0]
        log['time'] = re.compile(r':(.*)]').findall(raw_log)[0]
