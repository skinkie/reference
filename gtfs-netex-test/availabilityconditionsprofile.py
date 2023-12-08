from pathlib import Path
from typing import List, Dict, Tuple

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDuration, XmlTime

from GtfsNeTEx import date_to_xmldatetime
from netex import ServiceJourney, ServiceJourneyPattern, StopPointInJourneyPattern, TimetabledPassingTime, \
    PointsInJourneyPatternRelStructure, Codespace, TimetabledPassingTimesRelStructure, \
    PointInJourneyPatternRef, ServiceJourneyPatternRef, Call, MultilingualString, RouteView, Version, TimeDemandType, \
    DepartureStructure, ArrivalStructure, DatedCall, TimingLink, ScheduledStopPoint, TimingPointRefStructure, \
    JourneyRunTime, JourneyWaitTime, JourneyRunTimesRelStructure, TimingLinkRef, JourneyWaitTimesRelStructure, \
    ScheduledStopPointRef, TimingLinkRefStructure, PublicationDelivery, GeneralFrame, AvailabilityCondition, \
    ValidityConditionsRelStructure, AvailabilityConditionRef
from refs import getRef, getIndex, getId, getFakeRef, getBitString2
import sys
import copy
class AvailabilityConditionsProfile:
    codespace: Codespace
    version: Version

    def __init__(self, codespace: Codespace, version: Version):
        self.codespace = codespace
        self.version = version
    @staticmethod
    def getHexHash(hash_in: int):
        return ("%0.2X" % (hash_in**2))[0:8]

    def deduplicate(self, sjs: List[ServiceJourney]) -> (List[ServiceJourney], List[AvailabilityCondition]):
        sjs_operating_days = {}
        sjs_filtered = {}
        acs: Dict[str, AvailabilityCondition] = {}
        if sjs[0].calls and isinstance(sjs[0].calls.choice[0], DatedCall):
            for sj in sjs:
                dated_call: DatedCall = sj.calls.choice[0]
                key = '-'.join([sj.choice.ref, str(sj.departure_time).replace(':', '')])
                operating_dates = sjs_operating_days.get(key, set([]))
                operating_dates.add(dated_call.departure_date.to_datetime())
                sjs_operating_days[key] = operating_dates

                if key not in sjs_filtered:
                    sj = copy.deepcopy(sj)
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


if __name__ == '__main__':
    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    publication_delivery: PublicationDelivery = parser.from_path(Path("netex-output/wpd-tdts.xml"), PublicationDelivery)
    general_frame: GeneralFrame = publication_delivery.data_objects.choice[0]
    codespace: Codespace = general_frame.codespaces.codespace_ref_or_codespace[0]
    version: Version = general_frame.versions.version_ref_or_version[0]

    sjs: List[ServiceJourney] = [x for x in general_frame.members.choice if isinstance(x, ServiceJourney)]

    acp = AvailabilityConditionsProfile(codespace=codespace, version=version)

    sjs, acs = acp.deduplicate(sjs)

    general_frame.members.choice = [x for x in general_frame.members.choice if not isinstance(x, ServiceJourney)] + acs + sjs

    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(serializer_config)

    with open('netex-output/wpd-tdts-dedup.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)