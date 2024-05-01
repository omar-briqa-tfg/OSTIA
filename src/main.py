from src.filter.without_ipaddress   import WithoutIpAddress
from src.filter.with_ipv6address    import WithIPv6Address
from src.filter.access_resource     import AccessResource
from src.filter.search_resource     import SearchResource
from src.filter.web_resource        import WebResource

log = "111.11.11.111 - - [31/Mar/2023:00:00:01 +0200]"

_ = WithoutIpAddress.filter(log)

_ = WithIPv6Address.filter(log)

_ = AccessResource.filter(log)

_ = SearchResource.filter(log)

_ = WebResource.filter(log)
