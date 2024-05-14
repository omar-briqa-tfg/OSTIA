from src.metadata.filter.filter_interface import IFilter

from src.metadata.utils.constants import RECORD_DELETED

class RecordDeleted(IFilter):

    @classmethod
    def filter(cls, record: dict) -> bool:
        return record['header']['@status'] == RECORD_DELETED
