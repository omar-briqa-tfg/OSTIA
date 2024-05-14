from src.metadata.parser.dim_parser import DimParser

from src.metadata.filter.record_deleted import RecordDeleted

from src.metadata.oaipmh.oaiclient import OAIClient

import os
import json
import xmltodict


def process_metadata(client: OAIClient, resumptionToken: str | None) -> tuple[list[dict], str]:

    metadataList = []
    records, resumption_token = client.get_records(resumptionToken=resumptionToken)

    endOfRecords = 100
    while endOfRecords > 0:

        record = records.next()
        data = xmltodict.parse(str(record))['record']

        if not RecordDeleted.filter(data):

            id = data['header']['identifier']
            setSpec = data['header']['setSpec']
            metadata_list = data['metadata']['mets']['dmdSec']['mdWrap']['xmlData']['dim:dim']['dim:field']

            metadata = {
                'identifier': id,
                'setSpec': setSpec,
                'metadata': DimParser.parse(metadata_list)[0]
            }
            metadataList.append(metadata)

        endOfRecords = endOfRecords - 1

    # TODO: forward

    return metadataList, resumption_token

URL = os.environ.get('UPCOMMONS_METADATA_URL')
METADATA_PREFIX = os.environ.get('UPCOMMONS_METADATA_PREFIX')

client = OAIClient(endpoint=URL, metadataPrefix=METADATA_PREFIX)

resumptionToken = None
for _ in range(XXX):
    metadata, resumptionToken = process_metadata(client, resumptionToken=resumptionToken)
    print(len(metadata), resumptionToken)
