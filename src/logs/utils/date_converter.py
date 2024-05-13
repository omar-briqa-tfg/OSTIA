from datetime import datetime


def to_iso_format(date: str, time: str) -> tuple[str, str]:

    date_iso = datetime.strptime(date, '%d/%b/%Y').date().isoformat()
    time_iso = datetime.strptime(time, '%H:%M:%S %z').time().isoformat()

    return date_iso, time_iso


def to_timestamp(date: str, time: str) -> int:

    return int(datetime.strptime(date + ' ' + time, '%d/%b/%Y %H:%M:%S %z').timestamp())
