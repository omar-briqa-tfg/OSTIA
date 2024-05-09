from src.forwarder.forwarder_interface import IForwarder

from src.utils.date_converter import to_timestamp

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS

import os


class InfluxDbForwarder(IForwarder):

    influxdb_org: str | None = None
    influxdb_url: str | None = None
    influxdb_token: str | None = None
    influxdb_bucket: str | None = None
    influxDbClient: InfluxDBClient | None = None

    @classmethod
    def forward(cls, log: dict, raw_log: str) -> int:

        data = [{
            'measurement': 'demo',
            'tags': cls._set_log_tags(log),
            'fields': cls._set_log_fields(log, raw_log),
            'time': to_timestamp(log['date'], log['time'])
        }]

        client_write_api = cls._get_influxdb_client_write()

        # TODO: do not overwrite logs with the same timestamp
        client_write_api.write(record=data, write_precision='s', org=cls.influxdb_org, bucket=cls.influxdb_bucket)

        return 0

    @staticmethod
    def _set_log_tags(log: dict) -> dict:
        if log['content'] == "error":
            return {'content': "error"}
        else:
            return {
                'type': log['type'],
                'content': log['content'],
                'method': log['request']['method'],
                'status_code': log['request']['status_code']
            }

    @staticmethod
    def _set_log_fields(log: dict, raw_log: str):
        if log['type'] == "recurs":
            return {
                'log': raw_log,
                'recurs': log['recurs']
            }
        else:
            return {'log': raw_log}

    @classmethod
    def _get_influxdb_client_write(cls) -> InfluxDBClient:
        # TODO: check race condition
        if cls.influxDbClient is None:
            cls._get_influxdb_credentials()
            cls.influxDbClient = InfluxDBClient(url=cls.influxdb_url, token=cls.influxdb_token).write_api(ASYNCHRONOUS)
        return cls.influxDbClient

    @classmethod
    def _get_influxdb_credentials(cls) -> None:
        cls.influxdb_org = os.environ.get('INFLUXDB_ORG')
        cls.influxdb_url = os.environ.get('INFLUXDB_URL')
        cls.influxdb_token = os.environ.get('INFLUXDB_TOKEN')
        cls.influxdb_bucket = os.environ.get('INFLUXDB_BUCKET')