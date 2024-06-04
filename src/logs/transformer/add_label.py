from src.logs.transformer.transformer_interface import ITransformer


class AddLabel(ITransformer):

    @classmethod
    def transform(cls, log: dict, label: str, value: str) -> None:
        """
        Updates the **log** represented as a dictionary to add a new pair of <label, value>.

        :param log: Log entry to be transformed.
        :type log: dict
        :param label: Label to be added to the **log**.
        :type label: str
        :param value: Value of *label+ to be added to the **log**
        :type value: str
        :return: None
        """
        log[label] = value
