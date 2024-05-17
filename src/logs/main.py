from src.logs.filter.web_resource import WebResource
from src.logs.filter.search_resource import SearchResource
from src.logs.filter.access_resource import AccessResource
from src.logs.filter.with_ipv6address import WithIPv6Address
from src.logs.filter.without_ipaddress import WithoutIpAddress
from src.logs.filter.access_resource_bitstream import AccessResourceBitstream


from src.logs.transformer.to_json import ToJSON
from src.logs.transformer.add_label import AddLabel
from src.logs.transformer.remove_ipv6address import RemoveIPv6Address
from src.logs.transformer.add_resource_id_label import AddResourceIdLabel
from src.logs.transformer.add_default_ipaddress import AddDefaultIpAddress

from src.logs.forwarder.influxdb_forwarder import InfluxDbForwarder

from src.logs.utils.constants import LABEL_VALUE
from src.logs.utils.constants import LABEL_TYPE, LABEL_TYPE_OTHERS, LABEL_TYPE_SEARCH, LABEL_TYPE_RESOURCE, LABEL_TYPE_RESOURCE_WEB
from src.logs.utils.constants import LABEL_CONTENT, LABEL_CONTENT_OK, LABEL_CONTENT_ERROR, LABEL_CONTENT_DIFFERENT

import os
import json
import time
from pathlib import Path


def process_log(line: str) -> dict:

    log = {}
    stats = {}

    if WithoutIpAddress.filter(line):
        line = AddDefaultIpAddress.transform(line)

    elif WithIPv6Address.filter(line):
        line = RemoveIPv6Address.transform(line)

    try:
        log, status = ToJSON.transform(line)
        resource = log['request']['resource']

    # TODO: add specific exception
    except:
        log = {
            LABEL_VALUE: line,
            LABEL_CONTENT: LABEL_CONTENT_ERROR
        }
        # InfluxDbForwarder.forward(log, line)

        stats[LABEL_CONTENT] = LABEL_CONTENT_ERROR
        return stats

    AddLabel.transform(log, LABEL_CONTENT, LABEL_CONTENT_OK if status == 0 else LABEL_CONTENT_DIFFERENT)

    if AccessResource.filter(resource):
        AddResourceIdLabel.transform(log, resource)
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_RESOURCE)
        stats[LABEL_TYPE] = LABEL_TYPE_RESOURCE

    elif AccessResourceBitstream.filter(resource):
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_RESOURCE)
        stats[LABEL_TYPE] = LABEL_TYPE_RESOURCE

    elif WebResource.filter(resource):
        stats[LABEL_TYPE] = LABEL_TYPE_RESOURCE_WEB
        return stats

    elif SearchResource.filter(resource):
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_SEARCH)
        stats[LABEL_TYPE] = LABEL_TYPE_SEARCH

    else:
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_OTHERS)
        stats[LABEL_TYPE] = LABEL_TYPE_OTHERS

    # InfluxDbForwarder.forward(log, line)

    return stats


year = 2006
totalLogs = 0
input_path = os.environ.get('LOGS_OUTPUT_PATH')

global_stats = {
    'total_logs': 0,
    LABEL_TYPE_RESOURCE: 0,
    LABEL_TYPE_SEARCH: 0,
    LABEL_TYPE_RESOURCE_WEB: 0,
    LABEL_TYPE_OTHERS: 0,
    LABEL_CONTENT_ERROR: 0,
    'time': 0.0
}

start_time = time.time()
for month in range(1, 12):

    folder = Path(input_path) / Path(str(year)) / Path(f'{month:02}')

    for day in range(1, 32):

        log_file = folder / Path(f'{year}-{month:02}-{day:02}.log')

        if log_file.exists():

            print(f'{year}-{month:02}-{day:02}.log ...')

            with open(log_file, mode='rb') as file:
                logs = file.readlines()
                totalLogs = totalLogs + len(logs)

                for log in logs:
                    stats = process_log(log.decode('utf-8', errors='ignore'))

                    if LABEL_CONTENT in stats:
                        global_stats[LABEL_CONTENT_ERROR] += 1
                    else:
                        global_stats[stats[LABEL_TYPE]] += 1

InfluxDbForwarder.close()
end_time = time.time()

global_stats['total_logs'] = totalLogs
global_stats['time'] = end_time - start_time

print(json.dumps(global_stats, indent=4))
