from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from io import RawIOBase
from lxml import etree

from netex import ScheduledStopPoint, StopPlace, Quay, PassengerStopAssignment, MobilityEnumeration, \
    PyschosensoryNeedEnumeration, CoveredEnumeration, Parking, ParkingVehicleEnumeration, ShelterEquipmentRef, \
    ShelterEquipment
from rrutils import *

from typing import Any, Dict, Iterable, Optional, Tuple, List
from xsdata.exceptions import XmlHandlerError
from xsdata.models.enums import EventType

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

    scheduled_stop_points: Dict[str, ScheduledStopPoint]
    stop_places: Dict[str, StopPlace]
    parkings: Dict[str, Parking]
    passenger_stop_assignment: List[PassengerStopAssignment]

    quayref_to_quay: Dict[str, Quay]
    scheduled_stop_point_ref_to_physical: Dict[str, (StopPlace, Quay)]

    def __init__(self, input_filename: str):
        context = XmlContext()
        config = ParserConfig(fail_on_unknown_properties=False)
        self.parser = XmlParser(context=context, config=config, handler=MyLxmlEventHandler)
        self.tree = etree.parse(input_filename)

        self.scheduled_stop_points = None
        self.stop_places = None
        self.passenger_stop_assignment = None

    def get_scheduled_stop_points(self) -> Dict[str, ScheduledStopPoint]:
        if self.scheduled_stop_points is None:
            self.scheduled_stop_points = {x.id: x for x in [self.parser.parse(element, ScheduledStopPoint) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ScheduledStopPoint")]}

        return self.scheduled_stop_points

    def get_stop_places(self) -> Dict[str, StopPlace]:
        if self.stop_places is None:
            self.stop_places = {x.id: x for x in [self.parser.parse(element, StopPlace) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}StopPlace")]}

        return self.stop_places

    def get_parking(self) -> Dict[str, Parking]:
        if self.parkings is None:
            self.parkings = {x.id: x for x in [self.parser.parse(element, Parking) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}Parking")]}

        return self.parkings

    def get_passenger_stop_assignment(self) -> List[PassengerStopAssignment]:
        if self.passenger_stop_assignment is None:
            self.passenger_stop_assignment = [self.parser.parse(element, PassengerStopAssignment) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}PassengerStopAssignment")]

        return self.passenger_stop_assignment

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
            for passenger_stop_assignment in self.get_passenger_stop_assignment():
                if passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:
                    self.scheduled_stop_point_ref_to_physical[passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = quayref_to_quay_stop_place[passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref]
                else:
                    self.scheduled_stop_point_ref_to_physical[
                        passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = (None, stop_places[passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref])

        return self.scheduled_stop_point_ref_to_physical

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

    def export_sp_coords(self, out: RawIOBase):
        write_text_comment(out,"STOP POINT COORDS")
        self.loc_stop_point_coords = tell(out)

        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            write2floats(self.out, scheduled_stop_point.location.latitude or 0.0, scheduled_stop_point.location.longitude or 0.0)

    def export_sp_names(self, out: RawIOBase):
        write_text_comment(out,"STOP POINT NAMES")

        stop_names = [scheduled_stop_point.name.value for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_nameidx = self.write_list_of_strings(stop_names)

    def export_sp_uris(self, out: RawIOBase):
        # stopid index was several times bigger than the string table. it's probably better to just store fixed-width ids.
        write_text_comment(out, "STOP_POINT IDS")
        stop_ids = [scheduled_stop_point.id for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_point_uris = self.write_list_of_strings(stop_ids)

    def export_sp_attributes(self, out: RawIOBase):
        write_text_comment(out,"STOP POINT ATTRIBUTES")
        self.loc_stop_point_attributes = tell(out)

        scheduled_stop_point_ref_to_physical = self.netex_timetable.get_scheduled_stop_point_ref_to_physical()
        parkings = self.netex_timetable.get_parking()

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
