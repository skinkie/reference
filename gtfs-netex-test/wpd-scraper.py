from typing import Dict, List

import requests
import datetime
import json
import time

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlTime, XmlDate, XmlDuration, XmlDateTime

from netex import ServiceJourney, Codespace, MultilingualString, Version, Route, VehicleType, VehicleTypeRef, RouteRef, \
    StatusEnumeration, CallsRelStructure, DatedCall, ScheduledStopPointView, ScheduledStopPointRef, ScheduledStopPoint, \
    ArrivalStructure, DepartureStructure, ServiceJourneyPatternRef, ServiceJourneyPattern, OnwardTimingLinkView, \
    PublicationDelivery, DataObjectsRelStructure, GeneralFrame, CodespacesRelStructure, VersionsRelStructure, \
    GeneralFrameMembersRelStructure, DataSource, Operator, OrganisationTypeEnumeration, AllModesEnumeration, \
    ContactStructure, OperatorActivitiesEnumeration, VersionTypeEnumeration, ParticipantRef
from refs import getId, getFakeRef, getRef

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

headers = {
    'User-Agent': 'openOV/1.0',
    'From': 'ndovloket+wpd@opengeo.nl'
}

"""
        "departureDate": "2023-12-09T08:00:00",
        "arrivalDate": "2023-12-09T08:20:00",
        "duration": 20,
        "route": "SASH",
        "isDelayed": false,
        "delayedDepartureDate": null,
        "destinationHarbor": "Holwerd",
        "originHarbor": "Ameland",
        "freePassengerCapacity": 42,
        "bookedVehicleCapacity": null,
        "bookedBicycleCapacity": null,
        "bookedPassengerCapacity": 0.875,
        "isExtraDeparture": false,
        "isLocked": false,
        "isBookable": true,
        "isBookableOnline": true,
        "isBookableOffline": true,
        "islandName": "Ameland",
        "isUnavailable": false,
        "resourceType": 2
"""

class WagenborgTimetable():
    codespace: Codespace
    version: Version
    ssps: Dict[str, ScheduledStopPoint]

    def __init__(self, codespace, version, ssps):
        self.codespace = codespace
        self.version = version
        self.ssps = ssps

    @staticmethod
    def shortenHarbor(name):
        if name == "Holwerd":
            return "HO"
        elif name == "Ameland":
            return "AM"
        elif name == "Lauwersoog":
            return "LA"
        elif name == "Schiermonnikoog":
            return "SC"

    @staticmethod
    def mapStatus(isUnavailable):
        if isUnavailable:
            return StatusEnumeration.INACTIVE


    def mapperToDatedCall(self, journey):
        origin = WagenborgTimetable.shortenHarbor(journey['originHarbor'])
        destination = WagenborgTimetable.shortenHarbor(journey['destinationHarbor'])
        if origin not in self.ssps:
            self.ssps[origin] = ScheduledStopPoint(id=getId(ScheduledStopPoint, self.codespace, origin), version=version.version, name=MultilingualString(value=journey['originHarbor']), for_boarding=True, for_alighting=True)
        if destination not in self.ssps:
            self.ssps[destination] = ScheduledStopPoint(id=getId(ScheduledStopPoint, self.codespace, destination), version=version.version, name=MultilingualString(value=journey['destinationHarbor']), for_boarding=True, for_alighting=True)

        departure = journey['departureDate'].replace(':', '').replace('-', '')

        duration_secs = journey['duration'] * 60

        return ServiceJourney(id=getId(ServiceJourney, self.codespace, f"{origin}-{destination}-{departure}"), version=self.version.version,
                       vehicle_type_ref=getFakeRef(getId(VehicleType, self.codespace, journey['resourceType']), VehicleTypeRef, self.version.version),
                       status_attribute=WagenborgTimetable.mapStatus(journey['isUnavailable']),
                       calls=CallsRelStructure(call=[
                           # TODO: Remove DatedCalls
                           DatedCall(id=getId(ServiceJourney, self.codespace, f"{origin}-{destination}-{departure}-{origin}"), version=self.version.version,
                                               departure_date = XmlDate.from_string(journey['departureDate'].split('T')[0]),
                                               departure = DepartureStructure(time=XmlTime.from_string(journey['departureDate'].split('T')[1]), for_boarding=True),
                                                onward_timing_link_view=OnwardTimingLinkView(run_time=XmlDuration(f"PT{duration_secs}S")),
                                               fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=getRef(self.ssps[origin])),
                           DatedCall(id=getId(ServiceJourney, self.codespace, f"{origin}-{destination}-{departure}-{destination}"), version=self.version.version,
                                     fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=getRef(self.ssps[destination]),
                                     arrival_date=XmlDate.from_string(journey['arrivalDate'].split('T')[0]),
                                     arrival=ArrivalStructure(time=XmlTime.from_string(journey['arrivalDate'].split('T')[1]), for_alighting=True))]),
                       journey_pattern_ref=ServiceJourneyPatternRef(ref=getId(ServiceJourneyPattern, self.codespace, journey['route']))
                       )

print("...")

if __name__ == '__main__':
    json_post = ["HOAM", "SHSA", "AMHO", "SASH", "SCLA", "SSSL", "LASC", "SLSS"]
    firstdate = datetime.date.today()
    days = 60

    codespace = Codespace(id="BISON:Codespace:WPD", xmlns_url="http://bison.dova.nu/ns/WPD", xmlns="WPD", description=MultilingualString(value="Wagenborg Passagiers Diensten"))
    version = Version(id=getId(Version, codespace, "1"), version="1",
                      version_type=VersionTypeEnumeration.BASELINE,
                      start_date=XmlDateTime.from_datetime(datetime.datetime.combine(firstdate, datetime.time.min)),
                      end_date=XmlDateTime.from_datetime(datetime.datetime.combine(firstdate + datetime.timedelta(days=days), datetime.time.min)))
    data_source = DataSource(id=getId(DataSource, codespace, "WPD"),
                             version=version.version,
                             name=MultilingualString(value="Wagenborg Passagiersdiensten"),
                             short_name=MultilingualString(value="WPD"),
                             description=MultilingualString(value="WPD"))

    operator = Operator(id=getId(Operator, codespace, "WPD"), version=version.version,
                        company_number="02300456",
                        name=MultilingualString(value="Wagenborg Passagiersdiensten"),
                        short_name=MultilingualString(value="WPD"),
                        legal_name=MultilingualString(value="Wagenborg Passagiersdiensten B.V."),
                        organisation_type=[OrganisationTypeEnumeration.OPERATOR],
                        primary_mode=AllModesEnumeration.FERRY,
                        contact_details=ContactStructure(url="https://www.wpd.nl/"),
                        customer_service_contact_details=ContactStructure(email="info@wpd.nl",
                                                                          phone="+31881031000",
                                                                          url="https://www.wpd.nl/"),
                        operator_activities=[OperatorActivitiesEnumeration.PASSENGER])
    ssps = {}
    sjs = []

    wbt = WagenborgTimetable(codespace, version, ssps)

    session = requests.Session()
    for i in range(1, days):
        departure_date = firstdate + datetime.timedelta(days=i)
        document = session.post(f"https://api.wpd.nl/api/v1/Departures/overview/{departure_date}", json=json_post, headers=headers).json()
        sjs += [wbt.mapperToDatedCall(journey) for journey in document]
        time.sleep(0.200)

    general_frame = GeneralFrame(id=getId(GeneralFrame, codespace, "WPD"),
                                 versions=VersionsRelStructure(version_ref_or_version=[version]),
                                 codespaces=CodespacesRelStructure(codespace_ref_or_codespace=[codespace]),
                                 members=GeneralFrameMembersRelStructure(choice=[data_source] + [operator] + list(ssps.values()) + sjs)
                                 )

    publication_delivery = PublicationDelivery(
        publication_timestamp=XmlDateTime.now(),
        participant_ref=ParticipantRef(value="NDOV"),
        description=MultilingualString(value="Ruwe data WPD"),
        data_objects=DataObjectsRelStructure(choice=[general_frame]),
        version="ntx:1.1",
    )

    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(config=serializer_config)

    with open('netex-output/wpd-raw.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)

    print("...")