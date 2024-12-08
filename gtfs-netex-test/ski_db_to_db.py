import sys
from decimal import Decimal, ROUND_HALF_UP
from functools import partial
from itertools import chain
from typing import List, Iterable, T, Generator

from pyproj import Transformer, CRS
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netexio.database import Database
from netex import Codespace
from transformers.responsibilityset import infer_operator_from_responsibilityset_and_apply
from transformers.scheduledstoppoint import infer_locations_from_quay_or_stopplace_and_apply

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

import netex_monkeypatching

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def main(source_database_file: str):
    with Database(source_database_file, read_only=False) as db:
        infer_operator_from_responsibilityset_and_apply(db, db, generator_defaults)
        infer_locations_from_quay_or_stopplace_and_apply(db, db, generator_defaults)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Convert a NeTEx file to Dutch objects')
    argument_parser.add_argument('original', type=str, help='The original DuckDB NeTEx database')
    args = argument_parser.parse_args()

    main(args.original)


