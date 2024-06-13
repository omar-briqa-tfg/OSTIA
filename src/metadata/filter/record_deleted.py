from src.metadata.filter.filter_interface import IFilter

from src.metadata.utils.constants import RECORD_DELETED, HEADER_STATUS_KEY


class RecordDeleted(IFilter):

    @classmethod
    def filter(cls, record: dict) -> bool:
        """
        Determines if the metadata record is marked as deleted.

        :param record: The record entry to be checked.
        :type record: dict
        :return: True if the metadata entry contains the deleted status label.
        :rtype: bool
        """
        return (HEADER_STATUS_KEY in record['header'] and
                record['header'][HEADER_STATUS_KEY] == RECORD_DELETED)
