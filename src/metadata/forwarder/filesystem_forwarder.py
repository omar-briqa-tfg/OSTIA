from src.metadata.forwarder.forwarder_interface import IForwarder

from src.metadata.utils.constants import SIZE_RECORDS_LIST

import os
import json
from pathlib import Path


class FileSystemForwarder(IForwarder):

    folder_size = 1000
    output_path = Path(os.environ.get('METADATA_OUTPUT_PATH'))

    @classmethod
    def forward(cls, metadata_list: list[dict], batch: int) -> int:

        folder = cls._get_subfolder(batch)
        filename = f'{str(batch)}_{str(batch + SIZE_RECORDS_LIST)}.metadata.json'

        file = folder / Path(filename)

        with open(file, 'w') as file:
            json.dump(metadata_list, file, ensure_ascii=False)

        return 0

    @classmethod
    def _get_subfolder(cls, batch: int) -> Path:

        batch = (batch // cls.folder_size) * cls.folder_size

        folder = f"batch_{str(batch)}_{str((batch + cls.folder_size))}"

        path = cls.output_path / Path(folder)

        if not path.exists():
            path.mkdir()

        return path
