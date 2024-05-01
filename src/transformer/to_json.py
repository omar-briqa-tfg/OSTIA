from src.transformer.transformer_interface import ITransformer

import re
from typing import Union

class ToJSON(ITransformer):

    @classmethod
    def transform(cls, log: str) -> Union[dict[str, any], int]:

        status = 0

        identification = re.compile(r'(^\d.*]) \"').findall(log)[0]
        body = re.compile(r'(\".*)').findall(log)[0]

        ip = re.match(r'([0-9]+\.){3}[0-9]+', identification).group()
        date = re.compile(r'\d{1,2}/\w{3}/\d{1,4}').findall(identification)[0]
        time = re.compile(r':(.*)]').findall(identification)[0]

        http_description = re.compile(r'"([^"]*)"').findall(body)
        http_request = re.compile(r'(\S+)').findall(http_description[0])

        if len(http_request) != 3 or "HTTP" not in http_request[2]:

            http_description = [
                re.compile(r'"(.*HTTP\/\d.\d)"').findall(body)[0],
                re.compile(r'\s(-|\d+) "(.*)" ').findall(body)[0][1],
                re.compile(r'"\s"(.*)(|")$').findall(body)[0][0]
            ]

            http_request = re.compile(r'(^[A-Z]+)\s(.*)\s(HTTP\/\d.\d)$').findall(http_description[0])[0]
            status = -1

        http_request_method = http_request[0]
        http_request_resource = http_request[1]
        http_protocol_version = http_request[2]

        http_referer = http_description[1]
        http_user_agent = http_description[2]

        http_request_status_code = re.compile(r' (\d+) (-|\d+) ').findall(body)[0][0]
        http_request_response_size = re.compile(r' (\d+) (-|\d+) ').findall(body)[0][1]

        logJSON = {
            'ip_address': ip,
            'date': date,
            'time': time,
            'request': {
                'method': http_request_method,
                'resource': http_request_resource,
                'version': http_protocol_version,
                'status_code': http_request_status_code,
                'response_size': http_request_response_size
            },
            'referer': http_referer,
            'user_agent': http_user_agent
        }

        return logJSON, status
