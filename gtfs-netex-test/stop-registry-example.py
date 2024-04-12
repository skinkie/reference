import csv
from decimal import Decimal
from typing import List, Generator, Iterator

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from netex import StopPlace, SimplePointVersionStructure, LocationStructure2, PublicationDelivery, MultilingualString, \
    DataObjectsRelStructure, CompositeFrame, FramesRelStructure, InfrastructureFrame, ServiceFrame, ResourceFrame, \
    SiteFrame, StopPlacesInFrameRelStructure, Vehicle, VehicleType, ParticipantRef


def transform(stations_csv: str) -> Iterator[StopPlace]:
    with open(stations_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            row: dict
            yield StopPlace(id=row['id'],
                      version="1",
                      name=MultilingualString(value=row['name']),
                      centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=Decimal(row['latitude']), longitude=Decimal(row['longitude']))) if row['latitude'] != '' and row['longitude'] != '' else None,
                      )

site_frame = SiteFrame(id="SiteFrame", version="1", stop_places=StopPlacesInFrameRelStructure(stop_place=list(transform('/home/skinkie/Downloads/stations.csv'))))

composite_frame = CompositeFrame(id="CompositeFrame", version="1", frames=FramesRelStructure(common_frame=[site_frame]))

publication_delivery = PublicationDelivery(
    publication_timestamp=XmlDateTime.now(),
    participant_ref=ParticipantRef(value="StopRegistry"),
    description=MultilingualString(value="StopRegistry"),
    data_objects=DataObjectsRelStructure(choice=[composite_frame]),
    version="ntx:1.1",
)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

with open('/tmp/stopregistry2.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)


VehicleType(type)