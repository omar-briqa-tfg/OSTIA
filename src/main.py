from src.filter.without_ipaddress import WithoutIpAddress

log = "111.11.11.111 - - [31/Mar/2023:00:00:01 +0200]"

_ = WithoutIpAddress.filter(log)
