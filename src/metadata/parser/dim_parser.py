from typing import Dict, List, Any

from src.metadata.parser.parser_interface import IParser


class DimParser(IParser):

    @classmethod
    def parse(cls, metadata: dict) -> list[dict]:
        """
        Returns a list of metadata entries adapted to the DIM (DSpace Intermediate Format) format.

        :param metadata: The metadata entry to be parsed.
        :type metadata: dict
        :return: List of the metadata values parsed in DIM.
        :rtype: list[dict]
        """

        upcommons_metadata: dict[str, list[Any] | Any] = {}

        for data in metadata:

            schema = data.get('@mdschema', None)
            element = data.get('@element', None)
            qualifier = data.get('@qualifier', None)
            lang = data.get('@lang', None)

            metadata_key = '.'.join([value for value in [schema, element, qualifier, lang] if value])
            metadata_value = data.get('#text', '').encode('latin-1', errors='ignore').decode('unicode-escape', errors='ignore')

            if metadata_key in upcommons_metadata:
                if not isinstance(upcommons_metadata[metadata_key], list):
                    upcommons_metadata[metadata_key] = [upcommons_metadata[metadata_key]]
                upcommons_metadata[metadata_key].append(metadata_value)
            else:
                upcommons_metadata[metadata_key] = metadata_value

        return [upcommons_metadata]
