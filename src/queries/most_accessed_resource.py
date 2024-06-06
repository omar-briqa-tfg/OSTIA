from influxdb_client import InfluxDBClient

import os
import json

influxdb_org = os.environ.get('INFLUXDB_ORG')
influxdb_url = os.environ.get('INFLUXDB_URL')
influxdb_token = os.environ.get('INFLUXDB_TOKEN')
influxdb_bucket = os.environ.get('INFLUXDB_BUCKET')

resources = {}
influxDbClient = InfluxDBClient(url=influxdb_url, token=influxdb_token).query_api()

for month in range(2, 32):

    query = f"""
    from(bucket: "upcommons")
    |> range(start: 2023-12-{month-1:02}T00:00:00Z, stop: 2023-12-{month:02}T00:00:00Z)
    |> filter(fn: (r) => r["_measurement"] == "tfg")
    |> filter(fn: (r) => r["_field"] == "recurs")
    """
    print(f'2023-12-{month-1:02}')

    results = influxDbClient.query(query=query, org=influxdb_org)

    for result in results:
        for record in result.records:
            value = record.get_value()
            if not '[' in value:
                if not value in resources:
                    resources[value] = 1
                else:
                    resources[value] += 1


print("Processing ...")

most_accessed = dict(sorted(resources.items(), key=lambda item: item[1], reverse=True)[:10])

print(json.dumps(most_accessed, indent=4))
