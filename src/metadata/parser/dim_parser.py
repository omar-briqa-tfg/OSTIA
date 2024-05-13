from src.metadata.parser.parser_interface import IParser


class DimParser(IParser):

    @classmethod
    def parse(cls, metadata: dict) -> list[dict]:

        upcommons_metadata = {}

        for data in metadata:

            schema = data.get('@mdschema', None)
            element = data.get('@element', None)
            qualifier = data.get('@qualifier', None)
            lang = data.get('@lang', None)

            metadata_key = '.'.join([value for value in [schema, element, qualifier, lang] if value])
            metadata_value = data.get('#text', '').encode('latin-1').decode('unicode-escape')

            if metadata_key in upcommons_metadata:
                if not isinstance(upcommons_metadata[metadata_key], list):
                    upcommons_metadata[metadata_key] = [upcommons_metadata[metadata_key]]
                upcommons_metadata[metadata_key].append(metadata_value)
            else:
                upcommons_metadata[metadata_key] = metadata_value


        return [upcommons_metadata]
