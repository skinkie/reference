import duckdb as sqlite3

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from anyintodbnew import setup_database, get_interesting_classes

from netex import Codespace

from transformers.direction import infer_directions_from_sjps_and_apply
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

from transformers.epip import epip_line_memory, epip_scheduled_stop_point_memory, epip_site_frame_memory, \
    epip_service_journey_generator, epip_remove_keylist_extensions
from transformers.epip import EPIP_CLASSES

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1, 'DefaultLocationsystem': 'EPSG:4326'} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def main(source_database_file: str, target_database_file: str):
    classes = get_interesting_classes(filter=EPIP_CLASSES)
    with sqlite3.connect(target_database_file) as con:
        setup_database(con, classes, True)
    epip_line_memory(source_database_file, target_database_file, generator_defaults)
    infer_locations_from_quay_or_stopplace_and_apply(source_database_file, target_database_file, generator_defaults)
    epip_scheduled_stop_point_memory(target_database_file, target_database_file, generator_defaults)
    epip_site_frame_memory(source_database_file, target_database_file, generator_defaults)
    epip_service_journey_generator(source_database_file, target_database_file, generator_defaults, None)
    infer_directions_from_sjps_and_apply(target_database_file, target_database_file, generator_defaults)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Transform the input into mandatory objects for the export of EPIP')
    parser.add_argument('source', type=str, help='DuckDB file to use as input of the transformation.')
    parser.add_argument('target', type=str, help='DuckDB file to overwrite and store contents of the transformation.')
    args = parser.parse_args()

    main(args.source, args.target)