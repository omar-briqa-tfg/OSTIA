from src.metadata.parser.dim_parser import DimParser
from src.metadata.parser.bitstream_parser import BitstreamParser

from src.metadata.oaipmh.oaiclient import OAIClient

import os


URL = os.environ.get('UPCOMMONS_METADATA_URL')
METADATA_PREFIX = os.environ.get('UPCOMMONS_METADATA_PREFIX')

client = OAIClient(endpoint=URL, metadataPrefix=METADATA_PREFIX)

records = client.get_records(resumptionToken=None)


# data = {}['record']

# id = data['header']['identifier']
# setSpec = data['header']['setSpec']
# bitstream_list = data['metadata']['mets']['fileSec']['fileGrp']
# metadata_list = data['metadata']['mets']['dmdSec']['mdWrap']['xmlData']['dim:dim']['dim:field']

# metadata = {
#     'identifier': id,
#     'setSpec': setSpec,
#     'metadata': DimParser.parse(metadata_list)[0],
#     'bitstreams': BitstreamParser.parse(bitstream_list)
# }
