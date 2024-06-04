from src.logs.transformer.transformer_interface import ITransformer


class AddDefaultIpAddress(ITransformer):

    WITHOUT_IPADDRESS = '-'
    DEFAULT_IPADDRESS = '0.0.0.0'

    @classmethod
    def transform(cls, log: str) -> str:
        """
        Updates the *log* to add a default ip address.

        :param log: Log entry to be transformed.
        :type log: str
        :return: The log where the ``WITHOUT_IPADDRESS`` is replaced by `DEFAULT_IPADDRESS`.
        :rtype: str
        """
        return log.replace(cls.WITHOUT_IPADDRESS, cls.DEFAULT_IPADDRESS, 1)
