import duckdb as sqlite3
import pytz
from isal import igzip_threaded
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.datatype import XmlDateTime, XmlDate

from epip_db_to_xml import load_generator
from netex import NaturalLanguageStringStructure, ServiceJourney, OperatingDay, DirectionRef, LineRef
from siri import ProductionTimetableDelivery, DatedTimetableVersionFrame, DatedVehicleJourneyStructure, ServiceDelivery, \
    ParticipantRefStructure, ResponseTimestamp, LineRefStructure, DirectionRefStructure
from transformers.siri import siri_dated_vehicle_journey_generator

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

ns_map = {'': 'http://www.siri.org.uk/siri'}
tzinfo = pytz.timezone('Europe/Amsterdam') # TODO: This is still something we want somewhere in the database.

def main(source_database_file: str, operating_day: OperatingDay, line_ref: LineRef, direction_ref: DirectionRef, output_filename: str):
    response_timestamp = ResponseTimestamp(value=XmlDateTime.now())
    with sqlite3.connect(source_database_file, read_only=True) as read_con:
        ptd = ProductionTimetableDelivery(
            version="2.0",
            response_timestamp=response_timestamp,
            dated_timetable_version_frame=[
                DatedTimetableVersionFrame(
                    recorded_at_time=XmlDateTime.now(tz=tzinfo),
                    line_ref=LineRefStructure(value=line_ref.ref),
                    direction_ref=DirectionRefStructure(value=direction_ref.ref),
                    dated_vehicle_journey=siri_dated_vehicle_journey_generator(read_con, operating_day, line_ref, direction_ref, tzinfo))
            ])

        sd = ServiceDelivery(
            response_timestamp=response_timestamp,
            producer_ref=ParticipantRefStructure(value="PyNeTExConv"),
            choice=[ptd]
        )

        if output_filename.endswith('.gz'):
            with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2*10**8, encoding='utf-8') as out:
                serializer.write(out, sd, ns_map)
        else:
            with open(output_filename, 'w', encoding='utf-8') as out:
                serializer.write(out, sd, ns_map)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Convert a NeTEx file to SIRI-PT')
    argument_parser.add_argument('original', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('operating_day', type=str, help='OperatingDay to export')
    argument_parser.add_argument('line_ref', type=str, help='LineRef to export')
    argument_parser.add_argument('direction_ref', type=str, help='DirectionRef to export')
    argument_parser.add_argument('output', type=str, help='Output filename for SIRI-PT')
    args = argument_parser.parse_args()

    main(args.original, OperatingDay(calendar_date=XmlDate.from_string(args.operating_day)),
         LineRef(ref=args.line_ref), DirectionRef(ref=args.direction_ref), args.output)

