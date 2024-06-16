from influxdb_client import InfluxDBClient

from pymongo import MongoClient

import os
import ast

influxdb_org = os.environ.get('INFLUXDB_ORG')
influxdb_url = os.environ.get('INFLUXDB_URL')
influxdb_token = os.environ.get('INFLUXDB_TOKEN')
influxdb_bucket = os.environ.get('INFLUXDB_BUCKET')

mongodb_url = os.environ.get('MONGODB_URL')
mongodb_database_name = os.environ.get('MONGODB_DATABASE')
mongodb_collection_name = os.environ.get('MONGODB_COLLECTION')

resources = {}
influxDbClient = InfluxDBClient(url=influxdb_url, token=influxdb_token).query_api()

mongoDbClient = MongoClient(mongodb_url)
mongoDbCollection = mongoDbClient[mongodb_database_name][mongodb_collection_name]

for day in range(2, 3):

    # |> range(start: 2023-12-{day-1:02}T00:00:00Z, stop: 2023-12-{day:02}T00:00:00Z)

    query = f"""
    from(bucket: "upcommons")
    |> range(start: 2023-12-01T00:00:00Z, stop: 2023-12-01T00:01:00Z)
    |> filter(fn: (r) => r["_measurement"] == "tfg")
    |> filter(fn: (r) => r["_field"] == "recurs")
    |> keep(columns: ["_value", "_time"])
    """

    results = influxDbClient.query(query=query, org=influxdb_org)

    for result in results:
        for record in result.records:
            ids = record.get_value()
            time = record.get_time()

            values = ast.literal_eval(ids) if '[' in ids else [ids]
            for value in values:

                mongo_query = {
                    'id': value
                }
                resource = mongoDbCollection.find_one(mongo_query)

                print(resource)
