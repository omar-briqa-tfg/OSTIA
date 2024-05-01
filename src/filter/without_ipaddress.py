from src.filter.filter_interface import IFilter

class WithoutIpAddress(IFilter):

    WITHOUT_IPADDRESS = '-'

    @classmethod
    def filter(self, log: str) -> bool:
        return (log[0] == self.WITHOUT_IPADDRESS)
