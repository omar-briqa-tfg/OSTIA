from src.filter.without_ipaddress   import WithoutIpAddress
from src.filter.with_ipv6address    import WithIPv6Address
from src.filter.access_resource     import AccessResource
from src.filter.search_resource     import SearchResource
from src.filter.web_resource        import WebResource

from src.transformer.add_default_ipaddress  import AddDefaultIpAddress
from src.transformer.remove_ipv6address     import RemoveIPv6Address
from src.transformer.to_json                import ToJSON

# _ = WithoutIpAddress.filter(log)
# _ = WithIPv6Address.filter(log)
# _ = AccessResource.filter(log)
# _ = SearchResource.filter(log)
# _ = WebResource.filter(log)

# _ = AddDefaultIpAddress.transform(log)
# _ = RemoveIPv6Address.transform(log)
# _ = ToJSON.transform(log)
