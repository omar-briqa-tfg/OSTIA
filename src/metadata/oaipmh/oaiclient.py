from sickle import Sickle
import xmltodict
import json
import os

URL = os.environ.get('UPCOMMONS_METADATA_URL')
METADATA_PREFIX = os.environ.get('UPCOMMONS_METADATA_PREFIX')

sickle = Sickle(endpoint=URL)
records = sickle.ListRecords(metadataPrefix=METADATA_PREFIX)

record = records.next()

print(json.dumps(xmltodict.parse(str(record)), indent=4))
