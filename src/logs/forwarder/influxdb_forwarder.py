from src.logs.forwarder.forwarder_interface import IForwarder

from src.logs.utils.date_converter import to_nanoseconds

from influxdb_client import InfluxDBClient, WriteApi
from influxdb_client.client.write_api import WriteOptions, WriteType

import os


class InfluxDbForwarder(IForwarder):

    influxdb_org: str | None = None
    influxdb_url: str | None = None
    influxdb_token: str | None = None
    influxdb_bucket: str | None = None
    influxDbClient: InfluxDBClient | None = None

    previous_timestamp: int = 0
    previous_date: tuple[str, str] = ('', '')

    @classmethod
    def forward(cls, log: dict, raw_log: str) -> int:
        """
        Forwards the **log** entry to InfluxDB.

        :param log: The processed log entry to be forwarded, represented as a dictionary.
        :type log: dict
        :param raw_log: The log entry to be checked.
        :type raw_log: str
        :return: Status code of the action.
        :rtype: int
        """

        try:
            time = cls._set_timestamp(log['date'], log['time'])
        except:
            return 1

        data = {
            'measurement': 'tfg',
            'tags': cls._set_log_tags(log),
            'fields': cls._set_log_fields(log, raw_log),
            'time': time
        }

        client_write_api = cls._get_influxdb_client_write()

        client_write_api.write(record=data, write_precision='ns', org=cls.influxdb_org, bucket=cls.influxdb_bucket)

        # TODO: return correct value
        return 0

    @classmethod
    def close(cls) -> None:
        """
        Close the *InfluxDB* write api client.

        :return: None
        """
        if cls.influxDbClient is not None:
            cls.influxDbClient.close()

    @staticmethod
    def _set_log_tags(log: dict) -> dict:
        """
        Defines the *InfluxDB* tags based on the content of the log entry.

        :param log: The log entry, represented as a dictionary.
        :type log: dict
        :return: A dictionary with the specific tags.
        :rtype: dict
        """
        if log['content'] == "error":
            return {'content': "error"}
        else:
            return {
                'content': log['content'],
                'method': log['request']['method'],
                'status_code': log['request']['status_code'],
                'type': log['type']
            }

    @staticmethod
    def _set_log_fields(log: dict, raw_log: str) -> dict:
        """
        Defines the *InfluxDB* fields based on the content of the log entry.

        :param log: The processed log entry to be forwarded, represented as a dictionary.
        :type log: dict
        :param raw_log: The log entry to be checked.
        :type raw_log: dict
        :return: A dictionary with the specific fields.
        :rtype: dict
        """
        if log.get('type') == 'recurs' and 'resource' in log:
            return {
                'log': raw_log,
                'recurs': str(log['resource'])
            }
        else:
            return {'log': raw_log}

    @classmethod
    def _get_influxdb_client_write(cls) -> WriteApi:
        """
        Returns the *InfluxDB* write client

        :return: *InfluxDB* write api client
        :rtype: WriteApi
        """
        if cls.influxDbClient is None:
            cls._get_influxdb_credentials()
            cls.influxDbClient = InfluxDBClient(
                url=cls.influxdb_url,
                token=cls.influxdb_token,
                enable_gzip=True
            ).write_api(
                write_options=WriteOptions(
                    write_type=WriteType.batching,
                    batch_size=5_000,
                    flush_interval=2_000
            ))
        return cls.influxDbClient

    @classmethod
    def _get_influxdb_credentials(cls) -> None:
        """
        Obtains *InfluxDB* credentials from environment variables.

        :return: None
        """
        cls.influxdb_org = os.environ.get('INFLUXDB_ORG')
        cls.influxdb_url = os.environ.get('INFLUXDB_URL')
        cls.influxdb_token = os.environ.get('INFLUXDB_TOKEN')
        cls.influxdb_bucket = os.environ.get('INFLUXDB_BUCKET')

    @classmethod
    def _set_timestamp(cls, date: str, time: str) -> int:
        """
        Converts the date, time pair in to a UNIX timestamp.

        At every collision with *previous_timestamp* one second is added.

        :param date: Date in dd-mm-yyyy format.
        :type date: str
        :param time: Time in hh:mm:ss z format.
        :type time: str
        :return: Timestamp of the <date,time> pair.
        :rtype: int
        """

        ts = to_nanoseconds(date, time)

        if (date, time) == cls.previous_date:
            ts = cls.previous_timestamp = cls.previous_timestamp + 1
        else:
            cls.previous_timestamp = ts

        cls.previous_date = (date, time)
        return ts
