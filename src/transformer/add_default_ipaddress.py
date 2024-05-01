from src.transformer.transformer_interface import ITransformer

class AddDefaultIpAddress(ITransformer):

    WITHOUT_IPADDRESS = '-'
    DEFAULT_IPADDRESS = '0.0.0.0'

    @classmethod
    def transform(cls, log: str) -> str:
        return log.replace(cls.WITHOUT_IPADDRESS, cls.DEFAULT_IPADDRESS, 1)
