from src.filter.without_ipaddress   import WithoutIpAddress
from src.filter.with_ipv6address    import WithIPv6Address
from src.filter.access_resource     import AccessResource
from src.filter.search_resource     import SearchResource
from src.filter.web_resource        import WebResource

from src.transformer.add_default_ipaddress  import AddDefaultIpAddress
from src.transformer.remove_ipv6address     import RemoveIPv6Address
from src.transformer.to_json                import ToJSON
from src.transformer.add_label              import AddLabel
from src.transformer.add_resource_id_label  import AddResourceIdLabel

def process_logs(line: str):

    log = {}

    if WithoutIpAddress.filter(line):
        line = AddDefaultIpAddress.transform(line)

    elif WithIPv6Address.filter(line):
        line = RemoveIPv6Address.transform(line)

    try:
        log, status = ToJSON.transform(line)
        resource = log['request']['resource']

    except:
        # TODO: create log with value and content=error
        return

    AddLabel.transform(log, 'content', 'ok' if status == 0 else 'diferent')

    if AccessResource.filter(resource):
        AddResourceIdLabel.transform(log, resource)
        AddLabel.transform(log, 'type', 'recurs')

    elif SearchResource.filter(resource):
        AddLabel.transform(log, 'type', 'cerca')

    elif WebResource.filter(resource):
        return

    else:
        AddLabel.transform(log, 'type', 'altres')
