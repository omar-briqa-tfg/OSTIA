from src.metadata.oaipmh.oaiclient import OAIClient

from src.metadata.parser.dim_parser import DimParser

from src.metadata.filter.record_deleted import RecordDeleted

from src.metadata.forwarder.filesystem_forwarder import FileSystemForwarder

from src.metadata.utils.get_resource_id import get_resource_id
from src.metadata.utils.constants import SIZE_RECORDS_LIST

import os
import json
import xmltodict


def process_metadata(client: OAIClient, resumptionToken: str | None, batch: int) -> str:

    metadataList = []
    records, resumption_token = client.get_records(resumptionToken=resumptionToken)

    endOfRecords = SIZE_RECORDS_LIST
    while endOfRecords > 0:

        try:
            record = records.next()

        except StopIteration:
            break

        data = xmltodict.parse(str(record))['record']

        if not RecordDeleted.filter(data):

            id = data['header']['identifier']
            setSpec = data['header']['setSpec']
            metadata_list = data['metadata']['mets']['dmdSec']['mdWrap']['xmlData']['dim:dim']['dim:field']

            metadata = {
                'id': get_resource_id(id),
                'identifier': id,
                'setSpec': setSpec,
                'metadata': DimParser.parse(metadata_list)[0]
            }
            metadataList.append(metadata)

        endOfRecords = endOfRecords - 1

    FileSystemForwarder.forward(metadata_list=metadataList, batch=(batch * int(SIZE_RECORDS_LIST)))

    return resumption_token

URL = os.environ.get('UPCOMMONS_METADATA_URL')
METADATA_PREFIX = os.environ.get('UPCOMMONS_METADATA_PREFIX')

client = OAIClient(endpoint=URL, metadataPrefix=METADATA_PREFIX)

iteration = 0
resumptionToken = None
while True:
    resumptionToken = process_metadata(client, resumptionToken=resumptionToken, batch=iteration)
    if resumptionToken is None:
        break
    iteration = iteration + 1