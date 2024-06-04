import os
import json
import xmltodict
from typing import Any, Optional, Iterator

from sickle import Sickle


class OAIClient:

    def __init__(self, endpoint: str, metadataPrefix: str) -> None:

        self.url: str = endpoint
        self.prefix: str = metadataPrefix
        self.client: Optional[Sickle] = Sickle(endpoint=endpoint)

    def get_records(self, resumptionToken: Optional[str]) -> tuple[Iterator, str]:
        """
        Obtains a metadata iterator that follows the value of the **resumptionToken**.

        :param resumptionToken: Resumption token needed for the getRecords OAI-PMH request.
        :type resumptionToken: Optional[str]
        :return: A tuple composed by an iterator over the metadata, and the next resumptionToken.
        :rtype: tuple[Iterator, str]
        """

        records = None

        if resumptionToken is None:
            records = self.client.ListRecords(metadataPrefix=self.prefix)

        else:
            records = self.client.ListRecords(resumptionToken=resumptionToken)

        return records, records.resumption_token.token
