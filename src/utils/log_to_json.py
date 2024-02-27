import os
import re
import json

SOURCE_FILE = os.environ.get('SOURCE_FILE')

fd = open(file=SOURCE_FILE, mode='r')
Lines = fd.readlines()

for line in Lines:

    identification = re.compile(r'(^\d.*])').findall(line)[0]
    body = re.compile(r'(\".*)').findall(line)[0]

    ip = re.match(r'([0-9]+\.){3}[0-9]+', identification).group()
    date = re.compile(r'\d{1,2}/\w{3}/\d{1,4}').findall(identification)[0]
    time = re.compile(r':(.*)]').findall(identification)[0]

    http_description = re.compile(r'"([^"]*)"').findall(body)

    http_request = re.compile(r'(\S+)').findall(http_description[0])
    http_request_method = http_request[0]
    http_request_resource = http_request[1]
    http_protocol_version = http_request[2]

    http_request_status_code = re.compile(r' (\d+) (-|\d+) ').findall(body)[0][0]
    http_request_response_size = re.compile(r' (\d+) (-|\d+) ').findall(body)[0][1]

    http_referer = http_description[1]
    http_user_agent = http_description[2]

    log = {
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

    print(json.dumps(log, indent=4))

fd.close()
