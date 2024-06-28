from datetime import timedelta
from pathlib import Path
from typing import List, Dict, Tuple

import lxml
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDuration, XmlTime

from gtfs_convert_to_db import date_to_xmldatetime
from netex import ServiceJourney, ServiceJourneyPattern, StopPointInJourneyPattern, TimetabledPassingTime, \
    PointsInJourneyPatternRelStructure, Codespace, TimetabledPassingTimesRelStructure, \
    PointInJourneyPatternRef, ServiceJourneyPatternRef, Call, MultilingualString, RouteView, Version, TimeDemandType, \
    DepartureStructure, ArrivalStructure, TimingLink, ScheduledStopPoint, TimingPointRefStructure, \
    JourneyRunTime, JourneyWaitTime, JourneyRunTimesRelStructure, TimingLinkRef, JourneyWaitTimesRelStructure, \
    ScheduledStopPointRef, TimingLinkRefStructure, PublicationDelivery, GeneralFrame, AvailabilityCondition, \
    ValidityConditionsRelStructure, AvailabilityConditionRef, ServiceCalendar, UicOperatingPeriod, \
    UicOperatingPeriodRef, DatedServiceJourney
from refs import getRef, getIndex, getId, getFakeRef, getBitString2
import sys
import copy

from utils import project


class AvailabilityConditionsProfile:
    codespace: Codespace
    version: Version

    def __init__(self, codespace: Codespace, version: Version):
        self.codespace = codespace
        self.version = version
    @staticmethod
    def getHexHash(hash_in: int):
        return ("%0.2X" % (hash_in**2))[0:8]

    def deduplicate(self, sjs: List[DatedServiceJourney]) -> (List[ServiceJourney], List[AvailabilityCondition]):
        sjs_operating_days = {}
        sjs_filtered = {}
        acs: Dict[str, AvailabilityCondition] = {}
        if sjs[0].calls and isinstance(sjs[0].calls.call[0], Call):
            for sj in sjs:
                call: Call = sj.calls.call[0]

                key = '-'.join([sj.journey_pattern_ref.ref, str(sj.departure_time).replace(':', '')])

                operating_dates_this = [sj.uic_operating_period.from_operating_day_ref_or_from_date.to_datetime() + timedelta(days=i) for i in
                                     range(0, len(sj.uic_operating_period.valid_day_bits)) if
                                     sj.uic_operating_period.valid_day_bits[i] == '1']
                # TODO
                # sj.uic_operating_period.

                operating_dates = sjs_operating_days.get(key, set([]))
                operating_dates = operating_dates.union(operating_dates_this)
                sjs_operating_days[key] = operating_dates

                if key not in sjs_filtered:
                    # sj = copy.deepcopy(sj)
                    sj = project(sj, ServiceJourney)
                    sj.calls = None
                    sj.id = key.replace('ServiceJourneyPattern', 'ServiceJourney')
                    sjs_filtered[key] = sj

            for key in sjs_filtered.keys():
                od = sorted(sjs_operating_days[key])
                ac_hash = AvailabilityConditionsProfile.getHexHash(hash(tuple(od)))
                if ac_hash not in acs:
                    ac = AvailabilityCondition(
                        id=getId(AvailabilityCondition, self.codespace, ac_hash),
                        version=self.version.version, is_available=True,
                        from_date=date_to_xmldatetime(od[0]),
                        to_date=date_to_xmldatetime(od[-1]),
                        valid_day_bits=getBitString2(od))
                    acs[ac_hash] = ac
                else:
                    ac = acs[ac_hash]

                sjs_filtered[key].validity_conditions_or_valid_between = ValidityConditionsRelStructure(choice=[getRef(ac)])

        return (list(sjs_filtered.values()), list(acs.values()))

    @staticmethod
    def mapUicOperatingPeriodToAvailabilityCondition(uic_operating_period: UicOperatingPeriod) -> AvailabilityCondition:
        ac = AvailabilityCondition(
            id=uic_operating_period.id.replace("UicOperatingPeriod", "AvailabilityCondition"),
            version=uic_operating_period.version, is_available=True,
            from_date=uic_operating_period.from_operating_day_ref_or_from_date,
            to_date=uic_operating_period.to_operating_day_ref_or_to_date,
            valid_day_bits=uic_operating_period.valid_day_bits)

        return ac

    def fromEPIPServiceCalendar(self, service_calendars: List[ServiceCalendar], service_journeys: List[ServiceJourney]) -> (List[AvailabilityCondition], List[ServiceJourney]):
        day_type_to_ac = {}
        for service_calendar in service_calendars:
            if isinstance(service_calendar.operating_periods.uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period[0], UicOperatingPeriod):
                uic_operating_periods = {x.id : x for x in service_calendar.operating_periods.uic_operating_period_ref_or_operating_period_ref_or_operating_period_or_uic_operating_period if isinstance(x, UicOperatingPeriod)}
                for x in service_calendar.day_type_assignments.day_type_assignment:
                    if x.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date.name_of_ref_class == "UicOperatingPeriod":
                        day_type_to_ac[x.day_type_ref.ref] = AvailabilityConditionsProfile.mapUicOperatingPeriodToAvailabilityCondition(uic_operating_periods[x.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date.ref])

        sjs = []
        for sj in service_journeys:
            sj = copy.deepcopy(sj)
            sj.validity_conditions_or_valid_between = ValidityConditionsRelStructure(choice=[getRef(day_type_to_ac[sj.day_types.day_type_ref[0].ref])])
            sj.day_types = None
            sjs.append(sj)

        return (list(day_type_to_ac.values()), sjs)

if __name__ == '__main__':
    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    # publication_delivery: PublicationDelivery = parser.from_path(Path("netex-output-epip/Flix_Line_001.xml"), PublicationDelivery)
    # general_frame: GeneralFrame = publication_delivery.data_objects.choice[0]
    # codespace: Codespace = general_frame.codespaces.codespace_ref_or_codespace[0]
    # version: Version = general_frame.versions.version_ref_or_version[0]

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    lxml_parser = lxml.etree.XMLParser(remove_blank_text=True)
    tree = lxml.etree.parse("netex-output-epip/Flix_Line_001.xml", parser=lxml_parser)

    codespaces = [parser.parse(element, Codespace) for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Codespace")]
    versions = [parser.parse(element, Version) for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Version")]
    if len(versions) == 0:
        versions.append(Version(id="version", version="1"))

    servicecalendars = [parser.parse(element, ServiceCalendar) for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceCalendar")]
    sjs = [parser.parse(element, ServiceJourney) for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney")]

    acp = AvailabilityConditionsProfile(codespace=codespaces[0], version=versions[0])
    acs, sjs = acp.fromEPIPServiceCalendar(servicecalendars, sjs)

    print("...")

    # sjs: List[ServiceJourney] = [x for x in general_frame.members.choice if isinstance(x, ServiceJourney)]

    # acp = AvailabilityConditionsProfile(codespace=codespace, version=version)

    # sjs, acs = acp.deduplicate(sjs)

    # general_frame.members.choice = [x for x in general_frame.members.choice if not isinstance(x, ServiceJourney)] + acs + sjs

    # serializer_config = SerializerConfig(ignore_default_attributes=True)
    # serializer_config.pretty_print = True
    # serializer_config.ignore_default_attributes = True
    # serializer = XmlSerializer(config=serializer_config)

    # with open('netex-output/wpd-tdts-dedup.xml', 'w') as out:
    #     serializer.write(out, publication_delivery, ns_map)