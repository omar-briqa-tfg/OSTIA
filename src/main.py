from src.filter.without_ipaddress   import WithoutIpAddress
from src.filter.with_ipv6address    import WithIPv6Address

log = "111.11.11.111 - - [31/Mar/2023:00:00:01 +0200]"

_ = WithoutIpAddress.filter(log)

_ = WithIPv6Address.filter(log)
