from src.transformer.transformer_interface import ITransformer

class AddLabel(ITransformer):

    @classmethod
    def transform(cls, log: dict, label: str, value: str) -> None:
        log[label] = value
