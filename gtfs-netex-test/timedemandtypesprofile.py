import dataclasses
from pathlib import Path
from typing import List, Dict, Tuple

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDuration, XmlTime

from netex import ServiceJourney, ServiceJourneyPattern, StopPointInJourneyPattern, TimetabledPassingTime, \
    PointsInJourneyPatternRelStructure, Codespace, TimetabledPassingTimesRelStructure, \
    PointInJourneyPatternRef, ServiceJourneyPatternRef, Call, MultilingualString, RouteView, Version, TimeDemandType, \
    DepartureStructure, ArrivalStructure, DatedCall, TimingLink, ScheduledStopPoint, TimingPointRefStructure, \
    JourneyRunTime, JourneyWaitTime, JourneyRunTimesRelStructure, TimingLinkRef, JourneyWaitTimesRelStructure, \
    ScheduledStopPointRef, TimingLinkRefStructure, PublicationDelivery, GeneralFrame, ServiceLink, \
    TimingPointInJourneyPattern
from refs import getRef, getIndex, getId, getFakeRef
import sys
class TimeDemandTypesProfile:
    codespace: Codespace
    version: Version

    @staticmethod
    def getRunTimeCall(departure: Call, arrival: Call) -> int:
        return ((arrival.arrival.day_offset or 0) * 86400 + arrival.arrival.time.hour * 3600 + arrival.arrival.time.minute * 60 + arrival.arrival.time.second) - ((departure.departure.day_offset or 0) * 86400 + departure.departure.time.hour * 3600 +  departure.departure.time.minute * 60 + departure.departure.time.second)


    @staticmethod
    def getWaitTimeCall(call: DatedCall) -> int:
        if call.arrival is not None and call.departure is not None:
            return (86400 * (call.departure_date.to_datetime() - call.arrival_date.to_datetime()).days) + ((call.departure.day_offset or 0) * 86400 + call.departure.time.hour * 3600 + call.departure.time.minute * 60 + call.departure.time.second) - ((call.arrival.day_offset or 0) * 86400 + call.arrival.time.hour * 3600 +  call.arrival.time.minute * 60 + call.arrival.time.second)

    @staticmethod
    def getWaitTimeDatedCall(dated_call: DatedCall) -> int:
        if dated_call.arrival is not None and dated_call.departure is not None:
            return (86400 * (dated_call.departure_date.to_datetime() - dated_call.arrival_date.to_datetime()).days) + ((dated_call.departure.day_offset or 0) * 86400 + dated_call.departure.time.hour * 3600 + dated_call.departure.time.minute * 60 + dated_call.departure.time.second) - ((dated_call.arrival.day_offset or 0) * 86400 + dated_call.arrival.time.hour * 3600 +  dated_call.arrival.time.minute * 60 + dated_call.arrival.time.second)

        return 0

    @staticmethod
    def getRunTimeDatedCall(departure: DatedCall, arrival: DatedCall) -> int:
        return (86400 * (arrival.arrival_date.to_datetime() - departure.departure_date.to_datetime()).days) + ((arrival.arrival.day_offset or 0) * 86400 + arrival.arrival.time.hour * 3600 + arrival.arrival.time.minute * 60 + arrival.arrival.time.second) - ((departure.departure.day_offset or 0) * 86400 + departure.departure.time.hour * 3600 +  departure.departure.time.minute * 60 + departure.departure.time.second)


    @staticmethod
    def getRunTimePassingTime(departure: TimetabledPassingTime, arrival: TimetabledPassingTime) -> XmlDuration:
        run_time_secs = ((arrival.arrival_day_offset or 0) * 86400 + arrival.arrival_time.hour * 3600 + arrival.arrival_time.minute * 60 + arrival.arrival_time.second) - ((departure.departure_day_offset or 0) * 86400 + departure.departure_time.hour * 3600 +  departure.departure_time.minute * 60 + departure.departure_time.second)
        return XmlDuration(value=f"PT{run_time_secs}S")

    @staticmethod
    def getWaitTimePassingTime(passing_time: TimetabledPassingTime) -> XmlDuration:
        if passing_time.waiting_time:
            return passing_time.waiting_time
        if passing_time.arrival_time is not None and passing_time.departure_time is not None:
            waiting_time_secs = ((passing_time.departure_day_offset or 0) * 86400 + passing_time.departure_time.hour * 3600 + passing_time.departure_time.minute * 60 + passing_time.departure_time.second) - ((passing_time.arrival_day_offset or 0) * 86400 + passing_time.arrival_time.hour * 3600 +  passing_time.arrival_time.minute * 60 + passing_time.arrival_time.second)
            return XmlDuration(value=f"PT{waiting_time_secs}S")

    @staticmethod
    def getTimeDemandTypeHash(tdt: TimeDemandType):
        # TODO: REVIEW and replace with hashlib.sha256 digest!!
        # TODO: Check if the output of this code is the same as inline
        l = [(x.run_time, x.timing_link_ref.ref) for x in tdt.run_times.journey_run_time] + [(x.wait_time, x.choice.ref) for x in tdt.wait_times.journey_wait_time]
        return hash(l)

    @staticmethod
    def getTimeDemandTypeHash2(native_runtime: List[Tuple[XmlDuration, str,]], native_waittime: List[Tuple[XmlDuration, str,]]):
        return hash('_'.join([str(x) + '-' + str(y) for x, y in native_runtime]) + '_' + '_'.join([str(x) + '-' + str(y) for x, y in native_waittime]))

    @staticmethod
    def getHexHash(hash_in: int):
        return ("%0.2X" % (hash_in**2))[0:8]

    @staticmethod
    def getServiceJourneyPatternHash(sjp: ServiceJourneyPattern):
        # TODO: This will work for the simple cases, but will fail for routes having the same sequence, but for example a different route_ref (for a different line_ref)
        return hash('-'.join([TimeDemandTypesProfile.getPointRefFromPointInJourneyPattern(x).ref for x in sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern]))

    def getTimeDemandTypeByTimes(self, service_journey: ServiceJourney, time_demand_types: Dict[str, TimeDemandType], time_demand_types_hash: Dict[int, str], ssps: Dict[str, ScheduledStopPoint], tls: Dict[str, TimingLink], run_times: List[Tuple[XmlDuration, str,]], wait_times: List[Tuple[XmlDuration, str,]]):
        tdt_hash = TimeDemandTypesProfile.getTimeDemandTypeHash2(run_times, wait_times)
        tdt_hash_hex = TimeDemandTypesProfile.getHexHash(tdt_hash)

        if tdt_hash not in time_demand_types_hash:
            order = 0

            tdt = TimeDemandType(id=getId(TimeDemandType, self.codespace, tdt_hash_hex),
                                 version=self.version.version,
                                 run_times=JourneyRunTimesRelStructure(
                                     journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, self.codespace,
                                                                               "{:s}-{:d}".format(tdt_hash_hex, (
                                                                                   order := order + 1))),
                                                                      # TODO make more elegant
                                                                      version=self.version.version,
                                                                      timing_link_ref=getRef(tls.get(x[1])),
                                                                      run_time=x[0]) for x in run_times]),
                                 wait_times=JourneyWaitTimesRelStructure(journey_wait_time=[JourneyWaitTime(
                                     id=getId(JourneyWaitTime, self.codespace,
                                              "{:s}-{:d}".format(tdt_hash_hex, (order := order + 1))),
                                     version=self.version.version,
                                     choice=getRef(ssps.get(x[1]), ScheduledStopPointRef),
                                     wait_time=x[0]) for x in wait_times if x[0].seconds > 0]))

            if len(tdt.wait_times.journey_wait_time) == 0:
                tdt.wait_times = None

            time_demand_types[tdt.id] = tdt
            time_demand_types_hash[tdt_hash] = tdt.id
        else:
            tdt = time_demand_types[time_demand_types_hash[tdt_hash]]

        service_journey.time_demand_type_ref = getRef(tdt)

    def getTimeDemandTypeByDatedCalls(self, service_journey: ServiceJourney, time_demand_types: Dict[str, TimeDemandType], time_demand_types_hash: Dict[int, str], ssps: Dict[str, ScheduledStopPoint], tls: Dict[str, TimingLink]):
        dated_calls: List[DatedCall] = sorted(service_journey.calls.choice, key=lambda c: c.order)
        run_times: List[Tuple[XmlDuration, str,]] = []
        wait_times: List[Tuple[XmlDuration, str,]] = []

        for i in range(0, len(dated_calls) - 1):
            run_time = XmlDuration(
                value="PT{:d}S".format(TimeDemandTypesProfile.getRunTimeDatedCall(dated_calls[i], dated_calls[i + 1])))
            wait_time = XmlDuration(value="PT{:d}S".format(TimeDemandTypesProfile.getWaitTimeDatedCall(dated_calls[i])))
            ssp = ssps[dated_calls[
                i].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref]
            ssp_next = ssps[dated_calls[
                i + 1].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref]

            if dated_calls[i].onward_timing_link_view and dated_calls[i].onward_timing_link_view.timing_link_ref and \
                    dated_calls[i].onward_timing_link_view.timing_link_ref in tls:
                tl_ref = dated_calls[i].onward_timing_link_view.timing_link_ref
            else:
                tl_ref = getId(TimingLink, self.codespace,
                               TimeDemandTypesProfile.getHexHash(hash(ssp.id + "-" + ssp_next.id)))

            if tl_ref not in tls:
                tls[tl_ref] = TimingLink(id=getId(TimingLink, self.codespace,
                                                  TimeDemandTypesProfile.getHexHash(hash(ssp.id + "-" + ssp_next.id))),
                                         version=self.version.version,
                                         from_point_ref=getRef(ssp, TimingPointRefStructure),
                                         to_point_ref=getRef(ssp_next, TimingPointRefStructure))

            run_times.append((run_time, tl_ref,))
            wait_times.append((wait_time, ssp.id,))

        self.getTimeDemandTypeByTimes(service_journey, time_demand_types, time_demand_types_hash, ssps, tls, run_times, wait_times)
        service_journey.departure_time = dated_calls[0].departure.time


    def getTimeDemandTypeByCalls(self, service_journey: ServiceJourney, time_demand_types: Dict[str, TimeDemandType], time_demand_types_hash: Dict[int, str], ssps: Dict[str, ScheduledStopPoint], tls: Dict[str, TimingLink]):
        calls: List[Call] = sorted(service_journey.calls.choice, key=lambda c: c.order)
        run_times: List[Tuple[XmlDuration, str,]] = []
        wait_times: List[Tuple[XmlDuration, str,]] = []

        for i in range(0, len(calls) - 1):
            run_time = XmlDuration(
                value="PT{:d}S".format(TimeDemandTypesProfile.getRunTimeCall(calls[i], calls[i + 1])))
            wait_time = XmlDuration(value="PT{:d}S".format(TimeDemandTypesProfile.getWaitTimeDatedCall(calls[i])))
            ssp = ssps[calls[
                i].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref]
            ssp_next = ssps[calls[
                i + 1].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref]

            if calls[i].onward_timing_link_view and calls[i].onward_timing_link_view.timing_link_ref and \
                    calls[i].onward_timing_link_view.timing_link_ref in tls:
                tl_ref = calls[i].onward_timing_link_view.timing_link_ref
            else:
                tl_ref = getId(TimingLink, self.codespace,
                               TimeDemandTypesProfile.getHexHash(hash(ssp.id + "-" + ssp_next.id)))

            if tl_ref not in tls:
                tls[tl_ref] = TimingLink(id=getId(TimingLink, self.codespace,
                                                  TimeDemandTypesProfile.getHexHash(hash(ssp.id + "-" + ssp_next.id))),
                                         version=self.version.version,
                                         from_point_ref=getRef(ssp, TimingPointRefStructure),
                                         to_point_ref=getRef(ssp_next, TimingPointRefStructure))

            run_times.append((run_time, tl_ref,))
            wait_times.append((wait_time, ssp.id,))

        self.getTimeDemandTypeByTimes(service_journey, time_demand_types, time_demand_types_hash, ssps, tls, run_times, wait_times)
        service_journey.departure_time = calls[0].departure.time

    @staticmethod
    def getObjectFromObject(obj, new_clazz, id=None):
        attributes = set([x.name for x in dataclasses.fields(new_clazz)]).intersection(set([x.name for x in dataclasses.fields(obj.__class__)]))
        new_obj = new_clazz(**{x: obj.__dict__[x] for x in attributes})
        if id is not None:
            new_obj.id = id
        return new_obj

    def getTimeDemandTypeByTimetabledPassingTimes(self, service_journey: ServiceJourney,
                                                  service_journey_patterns: Dict[str, ServiceJourneyPattern],
                                                  time_demand_types: Dict[str, TimeDemandType], time_demand_types_hash: Dict[int, str],
                                                  ssps: Dict[str, ScheduledStopPoint], tls: Dict[str, TimingLink], sls: Dict[str, ServiceLink]):
        pass_times: List[TimetabledPassingTime] = service_journey.passing_times.timetabled_passing_time
        run_times: List[Tuple[XmlDuration, str,]] = []
        wait_times: List[Tuple[XmlDuration, str,]] = []

        sjp: ServiceJourneyPattern = service_journey_patterns[service_journey.choice.ref]
        piss = {x.id: x for x in sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern}

        for i in range(0, len(pass_times) - 1):
            run_time = TimeDemandTypesProfile.getRunTimePassingTime(pass_times[i], pass_times[i + 1])
            wait_time = TimeDemandTypesProfile.getWaitTimePassingTime(pass_times[i])
            # dit moet uit het journey pattern komen, waarbij ook nog een onward timing link beschikbaar is
            pis = piss[pass_times[i].point_in_journey_pattern_ref.ref]
            if isinstance(pis, StopPointInJourneyPattern):
                pis: StopPointInJourneyPattern = pis
                ssp = pis.scheduled_stop_point_ref
                if pis.onward_timing_link_ref is not None:
                    tl_ref = pis.onward_timing_link_ref.ref
                elif pis.onward_service_link_ref is not None:
                    sl: ServiceLink = sls[pis.onward_service_link_ref.ref]
                    tl_ref = sl.id.replace('ServiceLink', 'TimingLink')
                    if tl_ref not in tls:
                        tls[tl_ref] = TimeDemandTypesProfile.getObjectFromObject(sl, TimingLink, tl_ref)
                    pis.onward_service_link_ref = None
                else:
                    # TODO should infer onwards
                    pass
            elif isinstance(pis, TimingPointRefStructure):
                # TODO: wellicht iets doen waarbij ssps alle mogelijke 'points' direct al heeft
                pass

            run_times.append((run_time, tl_ref,))
            wait_times.append((wait_time, ssp.ref,))

        self.getTimeDemandTypeByTimes(service_journey, time_demand_types, time_demand_types_hash, ssps, tls, run_times, wait_times)
        service_journey.departure_time = pass_times[0].departure_time

    def getTimeDemandType(self, service_journey: ServiceJourney,
                          service_journey_patterns: Dict[str, ServiceJourneyPattern],
                          time_demand_types: Dict[str, TimeDemandType],
                          time_demand_types_hash: Dict[int, str],
                          ssps: Dict[str, ScheduledStopPoint],
                          tls: Dict[str, TimingLink],
                          sls: Dict[str, ServiceLink]):

        if service_journey.time_demand_type_ref is not None and service_journey.time_demand_type_ref.ref in time_demand_types:
            return time_demand_types[service_journey.time_demand_type_ref.ref]

        if service_journey.calls is not None:
            if isinstance(service_journey.calls.call[0], DatedCall):
                self.getTimeDemandTypeByDatedCalls(service_journey, time_demand_types, time_demand_types_hash, ssps, tls)
            elif isinstance(service_journey.calls.call[0], Call):
                self.getTimeDemandTypeByCalls(service_journey, time_demand_types, time_demand_types_hash, ssps, tls)
        elif service_journey.passing_times is not None:
            self.getTimeDemandTypeByTimetabledPassingTimes(service_journey, service_journey_patterns, time_demand_types, time_demand_types_hash, ssps, tls, sls)



    @staticmethod
    def getPointRefFromPointInJourneyPattern(pis):
        if isinstance(pis, StopPointInJourneyPattern):
            return pis.scheduled_stop_point_ref
        elif isinstance(pis, TimingPointInJourneyPattern):
            return pis.choice_1

        return None

    def getServiceJourneyPattern(self, service_journey: ServiceJourney, service_journey_patterns: Dict[str, ServiceJourneyPattern], service_journey_patterns_hash: Dict[int, str],
                                 ssps: Dict[str, ScheduledStopPoint], tls: Dict[str, TimingLink]):
        if service_journey.choice is not None and service_journey.choice.ref in service_journey_patterns:
            # TODO zorg er voor dat hier de onwards in ieder geval zijn gezet
            sjp = service_journey_patterns[service_journey.choice.ref]
            piss = sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern
            for i in range(0, len(piss) - 1):
                if isinstance(piss[i], StopPointInJourneyPattern):
                    pis: StopPointInJourneyPattern = piss[i]
                    pis_next = piss[i+1]
                    if pis.onward_timing_link_ref is None and pis.onward_timing_link_ref is None:
                        ssp = ssps[TimeDemandTypesProfile.getPointRefFromPointInJourneyPattern(pis).ref]
                        ssp_next = ssps[TimeDemandTypesProfile.getPointRefFromPointInJourneyPattern(pis_next).ref]
                        tl_ref = getId(TimingLink, self.codespace,
                                       TimeDemandTypesProfile.getHexHash(hash(ssp.id + "-" +
                                                                              ssp_next.id)))
                        if tl_ref not in tls:
                            tls[tl_ref] = TimingLink(id=tl_ref,
                                                     version=self.version.version,
                                                     from_point_ref=getRef(ssp, TimingPointRefStructure),
                                                     to_point_ref=getRef(ssp_next, TimingPointRefStructure))

                        pis.onward_timing_link_ref=getRef(tls[tl_ref], TimingLinkRefStructure)

            return sjp

        if isinstance(service_journey.calls.call[0], DatedCall):
            dated_calls: List[DatedCall] = service_journey.calls.call
            ssps_in_seq: List[TimingPointRefStructure] = []
            onward_tls: List[str] = []

            for i in range(0, len(dated_calls)-1):
                ssp = getRef(ssps[dated_calls[i].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref], TimingPointRefStructure)
                ssp_next = getRef(ssps[dated_calls[i+1].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref], TimingPointRefStructure)

                if dated_calls[i].onward_timing_link_view and dated_calls[i].onward_timing_link_view.timing_link_ref and dated_calls[i].onward_timing_link_view.timing_link_ref in tls:
                    tl_ref = dated_calls[i].onward_timing_link_view.timing_link_ref
                else:
                    tl_ref = getId(TimingLink, self.codespace, TimeDemandTypesProfile.getHexHash(hash(ssp.ref + "-" + ssp_next.ref)))

                if tl_ref not in tls:
                    tls[tl_ref] = TimingLink(id=getId(TimingLink, self.codespace, TimeDemandTypesProfile.getHexHash(hash(ssp.ref + "-" + ssp_next.ref))), version=self.version.version,
                                                from_point_ref=ssp,
                                                to_point_ref=ssp_next)
                ssps_in_seq.append(ssp)
                onward_tls.append(tl_ref)

            ssps_in_seq.append(getRef(ssps[dated_calls[-1].fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view.ref], TimingPointRefStructure))

            sjp_hash = hash('-'.join(x.ref for x in ssps_in_seq))
            sjp_hash_hex = TimeDemandTypesProfile.getHexHash(sjp_hash)

            if sjp_hash not in service_journey_patterns_hash or service_journey_patterns[service_journey_patterns_hash[sjp_hash]].id != service_journey.journey_pattern_ref.ref:
                piss = [(i, ssps_in_seq[i], getFakeRef(onward_tls[i], TimingLinkRefStructure, version=self.version.version)) for i in range(0, len(ssps_in_seq) - 1)]
                piss.append((len(ssps_in_seq) - 1, ssps_in_seq[-1], None))

                id = getId(ServiceJourneyPattern, self.codespace, sjp_hash_hex)
                if service_journey.choice is not None:
                    id = service_journey.choice.ref
                suffix = id.split(':')[-1]

                sjp =  ServiceJourneyPattern(id=id,
                                             version=self.version.version,
                                             points_in_sequence=PointsInJourneyPatternRelStructure(
                                                 point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                                     StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, self.codespace, "{:s}-{:d}".format(suffix, x[0] + 1)),
                                                                               version=self.version.version,
                                                                               order=x[0] + 1,
                                                         scheduled_stop_point_ref=getRef(ssps[x[1].ref]), onward_timing_link_ref=x[2]) for x in piss]))


                service_journey_patterns[sjp.id] = sjp
                service_journey_patterns_hash[sjp_hash] = sjp.id
            else:
                sjp = service_journey_patterns[service_journey_patterns_hash[sjp_hash]]

            service_journey.choice = getRef(sjp)

    def __init__(self, codespace: Codespace, version: Version):
        self.codespace = codespace
        self.version = version

if __name__ == '__main__':
    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    publication_delivery: PublicationDelivery = parser.from_path(Path("netex-output-epip/Flix_Line_025.xml"), PublicationDelivery)
    general_frame: GeneralFrame = publication_delivery.data_objects.choice[0]
    codespace: Codespace = general_frame.codespaces.codespace_ref_or_codespace[0]
    version: Version = general_frame.versions.version_ref_or_version[0]

    ssps: Dict[str, ScheduledStopPoint] = {x.id: x for x in general_frame.members.choice if isinstance(x, ScheduledStopPoint)}
    sjs: List[ServiceJourney] = [x for x in general_frame.members.choice if isinstance(x, ServiceJourney)]
    sjps = {}
    sjps_hash = {}
    tls = {}
    sls = {}
    tdts = {}
    tdts_hash = {}

    tdtp = TimeDemandTypesProfile(codespace=codespace, version=version)

    for sj in sjs:
        tdtp.getServiceJourneyPattern(sj, sjps, sjps_hash, ssps, tls)
        tdtp.getTimeDemandType(sj, sjps, tdts, tdts_hash, ssps, tls, sls)

    general_frame.members.choice += list(sjps.values()) + list(tls.values()) + list(tdts.values())

    serializer_config = SerializerConfig(ignore_default_attributes=True)
    serializer_config.pretty_print = True
    serializer_config.ignore_default_attributes = True
    serializer = XmlSerializer(serializer_config)

    with open('netex-output/wpd-tdts.xml', 'w') as out:
        serializer.write(out, publication_delivery, ns_map)