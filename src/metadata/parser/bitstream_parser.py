from src.metadata.parser.parser_interface import IParser

from src.metadata.utils.regex_patterns import BITSTREAM

import re


class BitstreamParser(IParser):

    @classmethod
    def parse(cls, metadata: dict) -> list[dict]:

        upcommons_bistreams = []

        for bitstream in metadata:

            use =  bitstream.get('@USE', None)
            type = bitstream['file'].get('@MIMETYPE', None)
            href = bitstream['file']['FLocat'].get('@xlink:href')
            bitstream_id = re.compile(BITSTREAM).findall(href)[0]

            upcommons_bistreams.append({
                'use': use, 'type': type, 'href': href, 'bitstream_id': bitstream_id
            })

        return upcommons_bistreams
