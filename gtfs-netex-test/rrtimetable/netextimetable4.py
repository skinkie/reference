import collections

from itertools import groupby
import operator

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from io import RawIOBase
from lxml import etree
from xsdata.models.datatype import XmlTime, XmlDuration

from netex import ScheduledStopPoint, StopPlace, Quay, PassengerStopAssignment, MobilityEnumeration, \
    PyschosensoryNeedEnumeration, CoveredEnumeration, Parking, ParkingVehicleEnumeration, ShelterEquipmentRef, \
    ShelterEquipment, ServiceJourneyPattern, DestinationDisplay, ServiceJourney, MobilityFacilityEnumeration, \
    LuggageCarriageEnumeration, PassengerInformationFacilityEnumeration, AssistanceFacilityEnumeration, \
    PassengerCommsFacilityEnumeration, SanitaryFacilityEnumeration, BusSubmode, BusSubmodeEnumeration, \
    FlexibleServiceEnumeration, ReservationEnumeration, PathLink
from rrutils import *

from typing import Any, Dict, Iterable, Optional, Tuple, List, OrderedDict
from xsdata.exceptions import XmlHandlerError
from xsdata.models.enums import EventType

MIN_WAITTIME = 2 * 60 #2 minutes ( in seconds)

class MyLxmlEventHandler(LxmlEventHandler):
    def process_context(
        self,
        context: Iterable[Tuple[str, Any]],
        ns_map: Dict[Optional[str], str],
    ) -> Any:
        """Iterate context and push events to main parser.

        Args:
            context: The iterable lxml context
            ns_map: A namespace prefix-URI recorder map

        Returns:
            An instance of the class type representing the parsed content.
        """
        for event, element in context:
            if event == EventType.START:
                self.parser.start(
                    self.clazz,
                    self.queue,
                    self.objects,
                    element.tag,
                    element.attrib,
                    element.nsmap,
                )
            elif event == EventType.END:
                self.parser.end(
                    self.queue,
                    self.objects,
                    element.tag,
                    element.text,
                    element.tail,
                )
                # We omit this, so we can keep parsing the same document.
                # element.clear()

            elif event == EventType.START_NS:
                prefix, uri = element
                self.parser.register_namespace(ns_map, prefix or None, uri)
            else:
                raise XmlHandlerError(f"Unhandled event: `{event}`.")

        return self.objects[-1][1] if self.objects else None

class NeTExTimetable:
    parser: XmlParser
    tree: etree._ElementTree

    scheduled_stop_points: OrderedDict[str, ScheduledStopPoint]
    stop_places: OrderedDict[str, StopPlace]
    service_journey_patterns: OrderedDict[str, ServiceJourneyPattern]
    destination_displays: OrderedDict[str, DestinationDisplay]
    service_journeys: OrderedDict[str, ServiceJourney]

    parkings: Dict[str, Parking]
    passenger_stop_assignment: List[PassengerStopAssignment]
    quayref_to_quay: Dict[str, Quay]
    scheduled_stop_point_ref_to_physical: Dict[str, (StopPlace, Quay)]
    quay_ref_to_scheduled_stop_point_ref: Dict[str, str]
    path_links: List[PathLink]

    def __init__(self, input_filename: str):
        context = XmlContext()
        config = ParserConfig(fail_on_unknown_properties=False)
        self.parser = XmlParser(context=context, config=config, handler=MyLxmlEventHandler)
        self.tree = etree.parse(input_filename)

        self.scheduled_stop_points = None
        self.stop_places = None
        self.passenger_stop_assignment = None

    def get_passenger_stop_assignments(self) -> List[PassengerStopAssignment]:
        if self.passenger_stop_assignments is None:
            self.passenger_stop_assignments = [self.parser.parse(element, PassengerStopAssignment) for element in
                               self.tree.findall(".//{http://www.netex.org.uk/netex}PassengerStopAssignment")]

        return self.passenger_stop_assignments

    def get_path_links(self) -> List[PathLink]:
        if self.path_links is None:
            self.path_links = [self.parser.parse(element, PathLink) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}PathLink")]
        
        return self.path_links

    def get_service_journeys(self) -> Dict[str, ServiceJourney]:
        if self.service_journeys is None:
            self.service_journeys = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, ServiceJourney) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourney")]})

        return self.service_journeys

    def get_scheduled_stop_points(self) -> Dict[str, ScheduledStopPoint]:
        if self.scheduled_stop_points is None:
            self.scheduled_stop_points = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, ScheduledStopPoint) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ScheduledStopPoint")]})

        return self.scheduled_stop_points

    def get_stop_places(self) -> Dict[str, StopPlace]:
        if self.stop_places is None:
            self.stop_places = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, StopPlace) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}StopPlace")]})

        return self.stop_places

    def get_destination_displays(self) -> Dict[str, DestinationDisplay]:
        if self.destination_displays is None:
            self.destination_displays = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, DestinationDisplay) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}DestinationDisplay")]})

        return self.destination_displays

    def get_parkings(self) -> Dict[str, Parking]:
        if self.parkings is None:
            self.parkings = {x.id: x for x in [self.parser.parse(element, Parking) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}Parking")]}

        return self.parkings

    def get_quayref_to_quay_stop_place(self) -> Dict[str, Quay]:
        if self.quayref_to_quay is None:
            for stop_place in self.get_stop_places().values():
                for any in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    self.quayref_to_quay[any.id] = (any, stop_place)

        return self.quayref_to_quay

    def get_scheduled_stop_point_ref_to_physical(self) -> Dict[str, (StopPlace, Quay)]:
        if self.scheduled_stop_point_ref_to_physical is None:
            stop_places = self.get_stop_places()
            quayref_to_quay_stop_place = self.get_quayref_to_quay_stop_place()
            for passenger_stop_assignment in self.get_passenger_stop_assignments():
                if passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:
                    self.scheduled_stop_point_ref_to_physical[passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = quayref_to_quay_stop_place[passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref]
                else:
                    self.scheduled_stop_point_ref_to_physical[
                        passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = (None, stop_places[passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref])

        return self.scheduled_stop_point_ref_to_physical

    def get_service_journey_patterns(self) -> Dict[str, ServiceJourneyPattern]:
        if self.service_journey_patterns is None:
            self.service_journey_patterns = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, ServiceJourneyPattern) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourneyPattern")]})

        return self.service_journey_patterns


class Index2:
    parser: XmlParser
    tree: etree._ElementTree
    out: RawIOBase

    n_stops: int
    loc_stop_point_coords: int

    loc_for_string: dict
    strings: List[str]
    string_length: int

    netex_timetable: NeTExTimetable

    def put_string(self,string):
        if string in self.loc_for_string:
            return self.loc_for_string[string]
        self.loc_for_string[string] = self.string_length
        self.string_length += (len(string) + 1)
        self.strings.append(string)
        return self.loc_for_string[string]

    def write_stop_point_idx(self, scheduled_stop_point_ref: str):
        if self.n_stops <= 65535:
            writeshort(self.out, list(self.netex_timetable.scheduled_stop_points.keys()).index(scheduled_stop_point_ref))
        else:
            writeint(self.out, list(self.netex_timetable.scheduled_stop_points.keys()).index(scheduled_stop_point_ref))

    def write_stop_area_idx(self, index, stop_place_ref: str):
        if len(index.stop_points) <= 65535:
            writeshort(self.out, list(self.netex_timetable.stop_places.keys()).index(stop_place_ref))
        else:
            writeint(self.out, list(self.netex_timetable.stop_places.keys()).index(stop_place_ref))

    def write_list_of_strings(self, list_of_strings: List[str]):
        loc = tell(self.out)
        for x in list_of_strings:
            writeint(self.out, self.put_string(x or ''))
        return loc

    def __init__(self, netex_timetable: NeTExTimetable):

        self.out = None
        self.n_stops = 0
        self.loc_stop_point_coords = 0

        self.loc_for_string = {}
        self.strings = []
        self.string_length = 0

        self.netex_timetable = netex_timetable

    def export_sp_coords(self):
        write_text_comment(self.out,"STOP POINT COORDS")
        self.loc_stop_point_coords = tell(self.out)

        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            write2floats(self.out, scheduled_stop_point.location.latitude or 0.0, scheduled_stop_point.location.longitude or 0.0)
            self.n_stops += 1

    def export_sp_names(self):
        write_text_comment(self.out,"STOP POINT NAMES")

        stop_names = [scheduled_stop_point.name.value for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_nameidx = self.write_list_of_strings(stop_names)

    def export_sp_uris(self):
        # stopid index was several times bigger than the string table. it's probably better to just store fixed-width ids.
        write_text_comment(self.out, "STOP_POINT IDS")
        stop_ids = [scheduled_stop_point.id for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_point_uris = self.write_list_of_strings(stop_ids)

    def export_sp_attributes(self):
        write_text_comment(self.out,"STOP POINT ATTRIBUTES")
        self.loc_stop_point_attributes = tell(self.out)

        scheduled_stop_point_ref_to_physical = self.netex_timetable.get_scheduled_stop_point_ref_to_physical()
        parkings = self.netex_timetable.get_parkings()

        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            quay: Quay
            stop_place: StopPlace

            quay, stop_place = scheduled_stop_point_ref_to_physical[scheduled_stop_point.id]
            accessibility_assessment = stop_place.accessibility_assessment
            place_equipments = stop_place.place_equipments
            if quay is not None:
                accessibility_assessment = quay.accessibility_assessment
                place_equipments = quay.place_equipments

            stop_attribute = 0

            for suitability in accessibility_assessment.suitabilities.suitability:
                if suitability.suitable and suitability.mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need == MobilityEnumeration.WHEELCHAIR:
                    stop_attribute |= 1
                elif suitability.suitable and suitability.mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need == PyschosensoryNeedEnumeration.VISUAL_IMPAIRMENT:
                    stop_attribute |= 2

            if stop_place.covered == CoveredEnumeration.COVERED:
                stop_attribute |= 4

            if place_equipments is not None and len([element for element in place_equipments.choice if isinstance(element, ShelterEquipment)]):
                stop_attribute |= 4

            for parking_ref in stop_place.adjacent_sites.stop_place_ref_or_site_ref:
                parking = parkings[parking_ref.ref]
                for parking_vehicle_types in parking.parking_vehicle_types:
                    if parking_vehicle_types == ParkingVehicleEnumeration.CYCLE:
                        stop_attribute |= 8

                    # TODO: BicycleRent

                    elif parking_vehicle_types == ParkingVehicleEnumeration.CAR:
                        stop_attribute |= 32

            writebyte(self.out, stop_attribute)

    def export_journey_pattern_point_stop(self):
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()

        write_text_comment(self.out,"JOURNEY PATTERN POINT STOP")
        self.loc_journey_pattern_points = tell(self.out)
        self.offset_jpp = []
        offset = 0
        self.n_jpp = 0
        for service_journey_pattern in service_journey_patterns.values():
            self.offset_jpp.append(offset)
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                self.n_jpp += 1
                self.write_stop_point_idx(point_in_sequence.scheduled_stop_point_ref.ref)
                offset += 1

    def export_journey_pattern_point_attributes(self):
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()

        write_text_comment(self.out,"JOURNEY PATTERN POINT ATTRIBUTES")
        self.loc_journey_pattern_point_attributes = tell(self.out)
        self.offset_jpp_attributes = []
        offset = 0
        for service_journey_pattern in service_journey_patterns.values():
            self.offset_jpp_attributes.append(offset)
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                attr = 0
                if point_in_sequence.is_wait_point:
                    attr |= 1
                if point_in_sequence.for_boarding:
                    attr |= 2
                if point_in_sequence.for_alighting:
                    attr |= 4
                writebyte(self.out, attr)
                offset += 1

    def export_journey_pattern_point_headsigns(self):
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()
        destination_displays = self.netex_timetable.get_destination_displays()

        write_text_comment(self.out,"JOURNEY PATTERN POINT HEADSIGN")
        self.loc_journey_pattern_point_headsigns = tell(self.out)
        self.offset_jpp = []
        offset = 0
        for service_journey_pattern in service_journey_patterns.values():
            self.offset_jpp.append(offset)
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                writeint(self.out, self.put_string(destination_displays[point_in_sequence.destination_display_ref_or_destination_display_view.ref] or destination_displays[service_journey_pattern.destination_display_ref_or_destination_display_view.ref] or ''))
                offset += 1

    @staticmethod
    def to_seconds(xml_time: XmlTime, day_offset: int = 0):
        _time = xml_time.to_time()
        return ((day_offset or 0) * 24 + _time.hour) * 3600 + _time.minute * 60 + _time.second

    @staticmethod
    def to_seconds2(xml_duration: XmlDuration):
        return ((xml_duration.days or 0) * 24 + xml_duration.hour) * 3600 + xml_duration.minute * 60 + xml_duration.second


    def export_timedemandtypes(self):
        # This is the only structure we actually will do pre-processing on.
        # Our TimeDemandType consists from relative times, each from the first departure time.
        # This is different from how NeTEx models it, since it uses relative distances between stops (on TimingLinks)
        # and uses points for wait times.

        tentative: List[tuple] = []
        sj_to_tdt: Dict[str, int]
        self.sj_to_tdt = {}

        for service_journey in self.netex_timetable.service_journeys.values():
            first_departure_time = Index2.to_seconds(service_journey.passing_times.timetabled_passing_time[0].departure_time, service_journey.passing_times.timetabled_passing_time[0].departure_day_offset)
            relative_distances = []

            for timetabled_passing_time in service_journey.passing_times.timetabled_passing_time:
                current_arrival_time = None
                if timetabled_passing_time.arrival_time:
                    current_arrival_time = Index2.to_seconds(timetabled_passing_time.arrival_time, timetabled_passing_time.arrival_day_offset)

                if timetabled_passing_time.departure_time:
                    current_departure_time = Index2.to_seconds(timetabled_passing_time.departure_time, timetabled_passing_time.departure_day_offset)
                    if current_arrival_time is None:
                        current_arrival_time = current_departure_time
                else:
                    current_departure_time = current_arrival_time

                relative_distances += (current_arrival_time - first_departure_time, current_departure_time - first_departure_time,)

            _tuple = tuple(relative_distances)
            if _tuple not in tentative:
                tentative.append(_tuple)

            self.sj_to_tdt[service_journey.id] = tentative.index(_tuple)

        timedemandgroup_t = Struct('HH')
        write_text_comment(self.out,"TIME DEMAND TYPES")
        self.loc_timedemandgroups = tell(self.out)
        self.offset_for_timedemandgroup_uri: Dict[int, int] = {}
        tp_offset = 0
        for i in range(0, len(tentative)):
            self.offset_for_timedemandgroup_uri[i] = tp_offset
            for tpp in tentative[i]:
                self.out.write(timedemandgroup_t.pack(tpp[0] >> 2, tpp[1] >> 2))
                tp_offset += 1
        self.n_tpp = tp_offset

    @staticmethod
    def get_service_journey(service_journey: ServiceJourney) -> (int, int):
        departure_time = Index2.to_seconds(service_journey.passing_times.timetabled_passing_time[0].departure_time, service_journey.passing_times.timetabled_passing_time[0].departure_day_offset)
        vj_attr = 0

        if isinstance(service_journey.transport_submode.choice, BusSubmode):
            vj_attr |= (service_journey.transport_submode.choice == BusSubmodeEnumeration.SCHOOL_BUS) << 6

        for facility_set in service_journey.facilities.service_facility_set_ref_or_service_facility_set:
            if facility_set.mobility_facility_list is not None:
                vj_attr |= (MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS in facility_set.mobility_facility_list.value) << 0

            if facility_set.luggage_carriage_facility_list is not None:
                vj_attr |= (LuggageCarriageEnumeration.CYCLES_ALLOWED in facility_set.luggage_carriage_facility_list.value) << 1

            if facility_set.passenger_comms_facility_list is not None:
                vj_attr |= (PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY in facility_set.passenger_information_facility_list.value) << 2
                vj_attr |= (PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS in facility_set.passenger_information_facility_list.value) << 3

            if facility_set.assistance_facility_list is not None:
                vj_attr |= (AssistanceFacilityEnumeration.BOARDING_ASSISTANCE in facility_set.assistance_facility_list.value) << 4

            # TODO: vja_appropriate_signage

            if facility_set.passenger_comms_facility_list is not None:
                vj_attr |= (PassengerCommsFacilityEnumeration.FREE_WIFI in facility_set.passenger_comms_facility_list.value) << 7

            if facility_set.sanitary_facility_list is not None:
                vj_attr |= (SanitaryFacilityEnumeration.TOILET in facility_set.sanitary_facility_list.value) << 8

            # TODO: upstream
            if facility_set.service_reservation_facility_list is not None:
                vj_attr |= (ReservationEnumeration.RESERVATIONS_COMPULSORY in facility_set.service_reservation_facility_list.value) << 10

        if service_journey.flexible_service_properties_ref_or_flexible_service_properties is not None:
            vj_attr |= (service_journey.flexible_service_properties_ref_or_flexible_service_properties.flexible_service_type != FlexibleServiceEnumeration.NOT_FLEXIBLE) << 9

        return departure_time, vj_attr

    def export_vj_in_jp(self):
        service_journeys = list(self.netex_timetable.get_service_journeys().values())
        service_journeys.sort(key = operator.attrgetter('journey_pattern_ref.ref'))
        groups = groupby(service_journeys, operator.attrgetter('journey_pattern_ref.ref'))

        write_text_comment(self.out,"VEHICLE JOURNEYS USING JOURNEY_PATTERN")
        self.loc_vehicle_journeys = tell(self.out)
        tioffset = 0
        self.vj_ids_offsets = []
        vj_t = Struct('IHH')
        for service_journey_pattern_ref, service_journeys in groups:
            self.vj_ids_offsets.append(tioffset)
            for service_journey in service_journeys:
                departure_time, vj_attr = Index2.get_service_journey(service_journey)
                # TODO
                # assert (tioffset - index.vj_ids_offsets[vj._jp_idx]) == vj._jpvjoffset
                self.out.write(vj_t.pack(self.offset_for_timedemandgroup_uri[self.sj_to_tdt[service_journey.id]],
                                         (departure_time + self.global_utc_offset) >> 2, vj_attr))
                tioffset += 1

    def export_jpp_at_sp(self):
        journey_patterns_at_stop_point = {}
        service_journey_patterns: List[ServiceJourneyPattern] = list(self.netex_timetable.get_service_journey_patterns().values())
        for service_journey_pattern in service_journey_patterns:
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                _set = journey_patterns_at_stop_point.get(point_in_sequence.scheduled_stop_point_ref.ref, set([]))
                journey_patterns_at_stop_point[point_in_sequence.scheduled_stop_point_ref.ref].add(service_journey_pattern.id)

        service_journey_patterns_idx = [service_journey_pattern.id for service_journey_pattern in service_journey_patterns]

        write_text_comment(self.out,"JOURNEY_PATTERNS AT STOP")
        self.loc_jp_at_sp = tell(self.out)
        self.jpp_at_sp_offsets = []
        n_offset = 0
        for scheduled_stop_point in self.netex_timetable.scheduled_stop_points.values():
            journey_pattern_refs = journey_patterns_at_stop_point[scheduled_stop_point.id]
            self.jpp_at_sp_offsets.append(n_offset)
            for journey_pattern_ref in journey_pattern_refs:
                writeshort(self.out, service_journey_patterns_idx.index(journey_pattern_ref))
                n_offset += 1
        self.jpp_at_sp_offsets.append(n_offset) #sentinel
        self.n_jpp_at_sp = n_offset

    def export_transfers(self):
        passenger_stop_assignments = self.netex_timetable.get_passenger_stop_assignments()
        passenger_stop_assignments.sort(key=operator.attrgetter('taxi_stand_ref_or_quay_ref_or_quay.ref'))
        passenger_stop_assignments_by_quay_ref = groupby(passenger_stop_assignments, operator.attrgetter('taxi_stand_ref_or_quay_ref_or_quay.ref'))

        path_links2 = []
        path_links = self.netex_timetable.get_path_links()
        for path_link in path_links:
            for _from in passenger_stop_assignments_by_quay_ref.get(path_link.from_value.place_ref.ref, []):
                for _to in passenger_stop_assignments_by_quay_ref.get(path_link.to.place_ref.ref, []):
                    path_links2.append((_from, _to, Index2.to_seconds2(path_link.transfer_duration.default_duration)))

        path_links2.sort(key=operator.itemgetter(1))
        path_links_by_scheduled_stop_point_ref = groupby(path_links2, operator.itemgetter(1))

        print("saving transfer stops (footpaths)")
        write_text_comment(self.out,"TRANSFER TARGET STOPS")
        self.loc_transfer_target_stop_points = tell(self.out)

        self.transfers_offsets = []
        offset = 0
        transfertimes = []
        stop_point_waittimes = {}
        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            self.transfers_offsets.append(offset)
            if scheduled_stop_point.id not in path_links_by_scheduled_stop_point_ref:
                continue
            for _from, _to, _default_duration in path_links_by_scheduled_stop_point_ref[scheduled_stop_point.id]:
                if _from == _to:
                    stop_point_waittimes[_from] = _default_duration
                    continue
                self.write_stop_point_idx(_to)
                transfertimes.append(_default_duration)
                offset += 1
        assert len(transfertimes) == offset
        self.transfers_offsets.append(offset) #sentinel
        self.n_connections = offset

        print("saving transfer times (footpaths)")
        write_text_comment(self.out, "TRANSFER TIMES")
        self.loc_transfer_dist_meters = tell(self.out)

        for transfer_time in transfertimes:
            writeshort(self.out,(int(transfer_time) >> 2))

        self.loc_stop_point_waittime = tell(self.out)
        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            _wait_time = stop_point_waittimes.get(scheduled_stop_point.id, MIN_WAITTIME)
            writeshort(self.out,(int(_wait_time) >> 2))