from src.filter.filter_interface import IFilter

class WithoutIpAddress(IFilter):

    WITHOUT_IPADDRESS = '-'

    @classmethod
    def filter(cls, log: str) -> bool:
        return (log[0] == cls.WITHOUT_IPADDRESS)
