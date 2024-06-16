# Disclaimer
# This is a PoC trial code aiming to demo the interoperability between the logs and the metadata
# In order to make the analysis as eficient as possible, certain design decisions must be updated.
# get_metadata_rights_value and get_metadata_language_value should be O(1)
# InfluxDb write api should change to batching mode as it is in the InfluxDB log forwarder

from influxdb_client import InfluxDBClient

from pymongo import MongoClient

import os
import re
import ast

influxdb_org = os.environ.get('INFLUXDB_ORG')
influxdb_url = os.environ.get('INFLUXDB_URL')
influxdb_token = os.environ.get('INFLUXDB_TOKEN')
influxdb_bucket = os.environ.get('INFLUXDB_BUCKET')

mongodb_url = os.environ.get('MONGODB_URL')
mongodb_database_name = os.environ.get('MONGODB_DATABASE')
mongodb_collection_name = os.environ.get('MONGODB_COLLECTION')

influxDbClientRead  = InfluxDBClient(
    url=influxdb_url,
    token=influxdb_token).query_api()

influxDbClientWrite = InfluxDBClient(
    url=influxdb_url,
    token=influxdb_token,
    enable_gzip=True).write_api()

mongoDbClient = MongoClient(mongodb_url)
mongoDbCollection = mongoDbClient[mongodb_database_name][mongodb_collection_name]

rights_regex = re.compile(r"^dc-rights-access")
language_regex = re.compile(r"^dc-language-iso")

def get_metadata_rights_value(metadata: dict):

    for key in metadata:
        if rights_regex.match(key):
            return metadata[key]

    return None

def get_metadata_language_value(metadata: dict):

    for key in metadata:
        if language_regex.match(key):
            return metadata[key]

    return None

def push_entry_influxdb(handle, rights, language, time):

    language = [language] if isinstance(language, str) else language

    for lang in language:

        data = {
            'measurement': 'epsevg-language',
            'tags': {
                'lang': lang
            },
            'fields': {
                'recurs': handle,
            },
            'time': int(time.timestamp() * 1e9)
        }

        influxDbClientWrite.write(record=data, write_precision='ns', org=influxdb_org, bucket=influxdb_bucket)


    data = {
        'measurement': 'epsevg-rights',
        'tags': {
            'rights': rights,
        },
        'fields': {
            'recurs': handle,
        },
        'time': int(time.timestamp() * 1e9)
    }

    influxDbClientWrite.write(record=data, write_precision='ns', org=influxdb_org, bucket=influxdb_bucket)

FACULTY_KEYWORD = "vilanova"
for day in range(2, 32):

    query = f"""
    from(bucket: "upcommons")
    |> range(start: 2023-12-{day-1:02}T00:00:00Z, stop: 2023-12-{day:02}T00:00:05Z)
    |> filter(fn: (r) => r["_measurement"] == "tfg")
    |> filter(fn: (r) => r["_field"] == "recurs")
    |> keep(columns: ["_value", "_time"])
    """
    print(f"2023-12-{day-1:02}")

    results = influxDbClientRead.query(query=query, org=influxdb_org)

    for result in results:
        for record in result.records:
            ids = record.get_value()
            time = record.get_time()

            values = ast.literal_eval(ids) if '[' in ids else [ids]
            for handle in values:

                mongo_query = { 'id': handle }
                resource = mongoDbCollection.find_one(mongo_query)

                if resource:
                    metadata = resource.get('metadata', {})
                    faculties = metadata.get('dc-audience-mediator')

                    if faculties:
                        faculties = [faculties] if isinstance(faculties, str) else faculties
                        for faculty in faculties:
                            if FACULTY_KEYWORD in faculty.lower():
                                rights = get_metadata_rights_value(metadata)
                                language = get_metadata_language_value(metadata)

                                push_entry_influxdb(handle, rights, language, time)



mongoDbClient.close()
