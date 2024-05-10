from src.filter.web_resource import WebResource
from src.filter.search_resource import SearchResource
from src.filter.access_resource import AccessResource
from src.filter.with_ipv6address import WithIPv6Address
from src.filter.without_ipaddress import WithoutIpAddress

from src.transformer.to_json import ToJSON
from src.transformer.add_label import AddLabel
from src.transformer.remove_ipv6address import RemoveIPv6Address
from src.transformer.add_resource_id_label import AddResourceIdLabel
from src.transformer.add_default_ipaddress import AddDefaultIpAddress

from src.forwarder.influxdb_forwarder import InfluxDbForwarder

from src.utils.constants import LABEL_VALUE
from src.utils.constants import LABEL_TYPE, LABEL_TYPE_OTHERS, LABEL_TYPE_SEARCH, LABEL_TYPE_RESOURCE
from src.utils.constants import LABEL_CONTENT, LABEL_CONTENT_OK, LABEL_CONTENT_ERROR, LABEL_CONTENT_DIFFERENT


def process_log(line: str):

    log = {}

    if WithoutIpAddress.filter(line):
        line = AddDefaultIpAddress.transform(line)

    elif WithIPv6Address.filter(line):
        line = RemoveIPv6Address.transform(line)

    try:
        log, status = ToJSON.transform(line)
        resource = log['request']['resource']

    except:
        log = {
            LABEL_VALUE: line,
            LABEL_CONTENT: LABEL_CONTENT_ERROR
        }
        return InfluxDbForwarder.forward(log, line)

    AddLabel.transform(log, LABEL_CONTENT, LABEL_CONTENT_OK if status == 0 else LABEL_CONTENT_DIFFERENT)

    if AccessResource.filter(resource):
        AddResourceIdLabel.transform(log, resource)
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_RESOURCE)

    elif WebResource.filter(resource):
        return

    elif SearchResource.filter(resource):
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_SEARCH)

    else:
        AddLabel.transform(log, LABEL_TYPE, LABEL_TYPE_OTHERS)

    return InfluxDbForwarder.forward(log, line)
