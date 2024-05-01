from src.forwarder.forwarder_interface import IForwarder

class LokiForwarder(IForwarder):

    @classmethod
    def forward(cls, log: dict) -> int:
        pass
