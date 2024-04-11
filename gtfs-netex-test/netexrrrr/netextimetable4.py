import collections
from io import BufferedWriter

from itertools import groupby
import operator
from struct import Struct

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from lxml import etree
from xsdata.models.datatype import XmlTime, XmlDuration

from netex import ScheduledStopPoint, StopPlace, Quay, PassengerStopAssignment, MobilityEnumeration, \
    PyschosensoryNeedEnumeration, CoveredEnumeration, Parking, ParkingVehicleEnumeration, ShelterEquipmentRef, \
    ShelterEquipment, ServiceJourneyPattern, DestinationDisplay, ServiceJourney, MobilityFacilityEnumeration, \
    LuggageCarriageEnumeration, PassengerInformationFacilityEnumeration, AssistanceFacilityEnumeration, \
    PassengerCommsFacilityEnumeration, SanitaryFacilityEnumeration, BusSubmode, BusSubmodeEnumeration, \
    FlexibleServiceEnumeration, ReservationEnumeration, PathLink, Connection, ServiceJourneyInterchange, Line, \
    AllVehicleModesOfTransportEnumeration, AvailabilityCondition, Operator, VehicleType, TypeOfProductCategory, Route, \
    PresentationStructure

from typing import Any, Dict, Iterable, Optional, Tuple, List, OrderedDict, BinaryIO
from xsdata.exceptions import XmlHandlerError
from xsdata.models.enums import EventType

NUMBER_OF_DAYS = 32
MIN_WAITTIME = 2 * 60 #2 minutes ( in seconds)
MAX_INTERLINE_WAITTIME = 5 * 60 #5 minutes ( in seconds)
JP_NONE = 65535
VJ_NONE = 65535

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

class Writer:
    pass

class JSONWriter(Writer):
    intermediate: list
    out: dict[str, list]
    strings: OrderedDict[str, int]

    def __init__(self, filename: str):
        self.strings = collections.OrderedDict({})
        self.out = {}

    def save(self):
        import json
        json.dump(self.out, open('/tmp/timetable4.json', 'w'), indent=4)

    def write_vj(self, tdg, departure_time, vj_attr):
        self.intermediate.append((tdg, departure_time, vj_attr,))
        # vj_t = Struct('IHH')
        # (vj_t.pack(self.offset_for_timedemandgroup_uri[self.sj_to_tdt[service_journey.id]],
        #                    (departure_time + self.global_utc_offset) >> 2, vj_attr))

    def write_vjref(self, jpref, vjref):
        self.intermediate.append((jpref, vjref,))
        # vjref_t = Struct('HH')
        # self.out.write(vjref_t.pack(JP_NONE, VJ_NONE))

    def write_route(self, jp_offset, trip_id_offset, jp_n_jpp, jp_n_vj, jp_attribute, routeidx_offset, jp_min_time, jp_max_time):
        # route_t = Struct('2I6H')
        # jp_t_fields = [jpp_offsets, trip_ids_offsets, jp_n_jpp, jp_n_vj, jp_attributes, routeidx_offsets, jp_min_time, jp_max_time]
        # self.out.write(route_t.pack(jpp_offsets[-1]+1, 0, 0, 0, 0, 0, 0, 0)) #Sentinel

        self.intermediate.append((jp_offset, trip_id_offset, jp_n_jpp, jp_n_vj, jp_attribute, routeidx_offset, jp_min_time, jp_max_time))

    def write_timedemandgroup(self, arrival_time, departure_time):
        self.intermediate.append((arrival_time, departure_time))
        # timedemandgroup_t = Struct('HH')
        # self.out.write(timedemandgroup_t.pack(tpp[0] >> 2, tpp[1] >> 2))

    def write_stopstruct(self, sp_offset, transfer_offset):
        self.intermediate.append((sp_offset, transfer_offset))
        # struct_2i = Struct('II')
        # self.out.write(struct_2i.pack(*stop))

    def writeint(self, x):
        self.intermediate.append(int(x))

    def writeshort(self, x):
        self.intermediate.append(int(x))

    def writebyte(self, x):
        self.intermediate.append(int(x))

    def writesignedbyte(self, x):
        self.intermediate.append(int(x))

    def write_2ushort(self, x, y):
        """Write coordinate (x,y) as packed binary data to file
        :param out: output file-pointer
        :param x: short with x-coordinate
        :param y: short with y-coordinate
        """
        self.intermediate.append([float(x), float(y)])

    def write2floats(self, x, y):
        self.intermediate.append([float(x), float(y)])

    def tell(self):
        """ Display the current output file position in a human-readable format, then return that position in bytes.
        :param out: output filepointer
        :return: current output file position
        """
        return len(self.intermediate)

    def write_text_comment(self, string: str):
        """ Write a text block to the file, just to help indentify segment boundaries, and align.
        :param out: output filepointer
        :param string: text comment
        """
        self.out[string] = []
        self.intermediate = self.out[string]

    def write_string(self, string: str):
        self.intermediate.append(string)

    def write_string_table(self, strings):
        for s in strings:
            self.intermediate.append(s)

    def put_string(self,string):
        location = self.strings.get(string, None)
        if location is not None:
            return location

        # self.strings[string] = self.string_length (binary variant)
        location = len(self.strings.keys())
        self.strings[string] = len(self.strings.keys())
        # self.string_length += (len(string) + 1) (binary variant)
        return location


class BinaryWriter(Writer):
    out: BinaryIO
    strings: OrderedDict[str, int]
    string_length: int

    struct_header = Struct('8sQi91I')

    def __init__(self, filename: str):
        self.out = open(filename, 'wb')
        self.out.seek(self.struct_header.size)

        self.string_length = 0
        self.strings = collections.OrderedDict({})

    def write_header(self):
        """ Write out a file header containing offsets to the beginning of each subsection.
        Must match struct transit_data_header in transitdata.c
        :param out: output filepointer
        :param index: Index of the datastructure exported
        """

        self.out.seek(0)
        htext = "TTABLEV4"
        self.out.write(packed)

    def save(self):
        self.out.close()

    def write_vj(self, tdg, departure_time, vj_attr):
        vj_t = Struct('IHH')
        self.out.write(vj_t.pack(tdg, departure_time, vj_attr))

    def write_vjref(self, jpref, vjref):
        vjref_t = Struct('HH')
        self.out.write(vjref_t.pack(jpref, vjref))

    def write_route(self, jp_offset, trip_id_offset, jp_n_jpp, jp_n_vj, jp_attribute, routeidx_offset, jp_min_time, jp_max_time):
        route_t = Struct('2I6H')
        self.out.write(route_t.pack(jp_offset, trip_id_offset, jp_n_jpp, jp_n_vj, jp_attribute, routeidx_offset, jp_min_time, jp_max_time))

    def write_timedemandgroup(self, arrival_time, departure_time):
        timedemandgroup_t = Struct('HH')
        self.out.write(timedemandgroup_t.pack(arrival_time, departure_time))

    def write_stopstruct(self, sp_offset, transfer_offset):
        struct_2i = Struct('II')
        self.out.write(struct_2i.pack(sp_offset, transfer_offset))

    def writeint(self, x):
        struct_1I = Struct('I') # a single UNSIGNED int
        """Write x as packed binary data to file
        :param out: output file-pointer
        :param x: unsigned int (0 <= x <= 4294967295)
        """
        self.out.write(struct_1I.pack(x))

    def writeshort(self, x):
        struct_1H = Struct('H') # a single UNSIGNED short
        """Write x as packed binary data to file
        :param out: output file-pointer
        :param x: unsigned short (0 <= x <= 65535)
        """
        self.out.write(struct_1H.pack(x))

    def writebyte(self, x):
        struct_1B = Struct('B')  # a single UNSIGNED byte
        """Write x as packed binary data to file
        :param out: output file-pointer
        :param x: unsigned byte (0 <= x <= 255)
        """
        self.out.write(struct_1B.pack(x))

    def writesignedbyte(self, x):
        struct_1b = Struct('b') # a single SIGNED byte
        """Write x as packed binary data to file
        :param out: output file-pointer
        :param x: signed byte (-128 <= x <= 127)
        """
        self.out.write(struct_1b.pack(x))

    def write_2ushort(self, x, y):
        struct_2H = Struct('HH') # two UNSIGNED shorts
        """Write coordinate (x,y) as packed binary data to file
        :param out: output file-pointer
        :param x: short with x-coordinate
        :param y: short with y-coordinate
        """
        self.out.write(struct_2H.pack(x, y))

    def write2floats(self, x, y):
        struct_2f = Struct("2f") # 2 floats
        """Write coordinate (x,y) as packed binary data to file
        :param out: output file-pointer
        :param x: float with x-coordinate
        :param y: float with y-coordinate
        """
        self.out.write(struct_2f.pack(float(x), float(y)))

    def align(self, width=4):
        """Align output file to a [width]-byte boundary.
        :param width: size of the boundary
        :param out: output file-pointer
        """
        pos = self.out.tell()
        n_padding_bytes = (width - (pos % width)) % width
        self.out.write(b'%' * n_padding_bytes)

    def tell(self) :
        """ Display the current output file position in a human-readable format, then return that position in bytes.
        :param out: output filepointer
        :return: current output file position
        """
        pos = self.out.tell()
        if pos > 1024 * 1024 :
            text = '%0.2f MB' % (pos / 1024.0 / 1024.0)
        else :
            text = '%0.2f kB' % (pos / 1024.0)
        print("  at position %d in output [%s]" % (pos, text))
        return pos

    def write_text_comment(self, string: str):
        """ Write a text block to the file, just to help indentify segment boundaries, and align.
        :param out: output filepointer
        :param string: text comment
        """
        string = '\r\n|| {:s} ||\r\n'.format(string)
        self.out.write(string.encode('utf-8'))
        self.align()

    def write_string(self, string: str):
        self.out.write(string.encode('utf-8') + b'\0')

    def write_string_table(self,strings):
        """ Write a table of fixed-width, null-terminated strings to the output file.
        The argument is a list of Python strings.
        The output string table begins with an integer indicating the width of each entry in bytes (including the null terminator).
        This is followed by N*W bytes of string data.
        This data structure can provide a mapping from integer IDs to strings and vice versa:
        If the strings are sorted, a binary search can be used for string --> ID lookups in logarithmic time.
        Note: Later we could use fixed width non-null-terminated string: printf("%.*s", length, string); or fwrite();
        :param out: output filepointer
        :param strings: list of strings
        """
        # sort a copy of the string list
        # strings = list(strings)
        # strings.sort()
        width = 0
        for s in strings :
            if len(s) > width :
                width = len(s)
        width += 1
        loc = self.tell()
        self.writeint(width)
        for s in strings.keys():
            self.out.write(s.encode('utf-8'))
            padding = b'\0' * (width - len(s))
            self.out.write(padding)
        return loc

    def put_string(self,string):
        location = self.strings.get(string, None)
        if location is not None:
            return location

        self.strings[string] = self.string_length
        self.string_length += (len(string) + 1)
        return self.strings[string]


class NeTExTimetable:
    parser: XmlParser
    tree: etree._ElementTree

    connections: List[Connection]
    # destination_displays: OrderedDict[str, DestinationDisplay]
    lines: OrderedDict[str, Line]
    operators: OrderedDict[str, Operator]
    quayref_to_quay: Dict[str, Quay]
    quay_ref_to_scheduled_stop_point_ref: Dict[str, str]
    parkings: Dict[str, Parking]
    passenger_stop_assignments: List[PassengerStopAssignment]
    routes: OrderedDict[str, Route]
    scheduled_stop_points: OrderedDict[str, ScheduledStopPoint]
    scheduled_stop_point_ref_to_physical: Dict[str, Tuple[StopPlace, Quay]]
    service_journey_patterns: OrderedDict[str, ServiceJourneyPattern]
    stop_places: OrderedDict[str, StopPlace]
    service_journeys: OrderedDict[str, ServiceJourney]
    service_journey_interchanges: List[ServiceJourneyInterchange]
    service_journey_patterns: Dict[str, ServiceJourneyPattern]
    service_journey_service_journey_pattern_group: Dict[str, List[ServiceJourney]]
    type_of_productcategories: OrderedDict[str, TypeOfProductCategory]


    def __init__(self, input_filename: str):
        context = XmlContext()
        config = ParserConfig(fail_on_unknown_properties=False)
        self.parser = XmlParser(context=context, config=config, handler=MyLxmlEventHandler)
        self.tree = etree.parse(input_filename)

        self.connections = None
        # self.destination_displays = None
        self.lines = None
        self.operators = None
        self.quayref_to_quay = None
        self.quay_ref_to_scheduled_stop_point_ref = None
        self.parkings = None
        self.passenger_stop_assignments = None
        self.routes = None
        self.scheduled_stop_points = None
        self.scheduled_stop_point_ref_to_physical = None
        self.service_journey_patterns = None
        self.stop_places = None
        self.service_journeys = None
        self.service_journey_interchanges = None
        self.service_journey_patterns = None
        self.service_journey_service_journey_pattern_group = None
        self.type_of_productcategories = None


    def get_service_journey_interchanges(self) -> List[ServiceJourneyInterchange]:
        if self.service_journey_interchanges is None:
            self.service_journey_interchanges = [self.parser.parse(element, ServiceJourneyInterchange) for element in
                               self.tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourneyInterchange")]

        return self.service_journey_interchanges

    def get_passenger_stop_assignments(self) -> List[PassengerStopAssignment]:
        if self.passenger_stop_assignments is None:
            self.passenger_stop_assignments = [self.parser.parse(element, PassengerStopAssignment) for element in
                               self.tree.findall(".//{http://www.netex.org.uk/netex}PassengerStopAssignment")]

        return self.passenger_stop_assignments

    def get_connections(self) -> List[Connection]:
        if self.connections is None:
            self.connections = [self.parser.parse(element, Connection) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}Connection")]
        
        return self.connections

    def get_lines(self) -> Dict[str, Line]:
        if self.lines is None:
            self.lines = collections.OrderedDict({line.id: line for line in [self.parser.parse(element, Line) for element in
                                self.tree.findall(".//{http://www.netex.org.uk/netex}Line")]})

        return self.lines

    def get_routes(self) -> Dict[str, Route]:
        if self.routes is None:
            self.routes = collections.OrderedDict({route.id: route for route in [self.parser.parse(element, Route) for element in
                                self.tree.findall(".//{http://www.netex.org.uk/netex}Route")]})

        return self.routes

    def get_operators(self) -> Dict[str, Operator]:
        if self.operators is None:
            operators = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, Operator) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}Operator")]})
            self.operators = operators

        # TODO: assert that there are less than 255 operators

        return self.operators

    def get_service_journeys(self) -> Dict[str, ServiceJourney]:
        if self.service_journeys is None:
            service_journeys = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, ServiceJourney) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ServiceJourney")]})
            for service_journey in service_journeys.values():
                service_journey._utc_offset = 0 # TODO: maybe directly do it here, and remove everywhere else?
                service_journey._departure_time_seconds = Index2.to_seconds(service_journey.passing_times.timetabled_passing_time[0].departure_time, service_journey.passing_times.timetabled_passing_time[0].departure_day_offset)
                service_journey._arrival_time_seconds = Index2.to_seconds(service_journey.passing_times.timetabled_passing_time[-1].arrival_time, service_journey.passing_times.timetabled_passing_time[-1].arrival_day_offset)

            self.service_journeys = service_journeys

        return self.service_journeys

    def get_scheduled_stop_points(self) -> Dict[str, ScheduledStopPoint]:
        if self.scheduled_stop_points is None:
            self.scheduled_stop_points = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, ScheduledStopPoint) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}ScheduledStopPoint")]})

        return self.scheduled_stop_points

    def get_stop_places(self) -> Dict[str, StopPlace]:
        if self.stop_places is None:
            self.stop_places = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, StopPlace) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}StopPlace")]})

        return self.stop_places

    # def get_destination_displays(self) -> Dict[str, DestinationDisplay]:
    #    if self.destination_displays is None:
    #        self.destination_displays = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, DestinationDisplay) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}DestinationDisplay")]})

    #     return self.destination_displays

    def get_parkings(self) -> Dict[str, Parking]:
        if self.parkings is None:
            self.parkings = {x.id: x for x in [self.parser.parse(element, Parking) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}Parking")]}

        return self.parkings

    def get_quayref_to_quay_stop_place(self) -> Dict[str, Quay]:
        if self.quayref_to_quay is None:
            self.quayref_to_quay = {}
            for stop_place in self.get_stop_places().values():
                for any in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    self.quayref_to_quay[any.id] = (any, stop_place)

        return self.quayref_to_quay

    def get_scheduled_stop_point_ref_to_physical(self) -> Dict[str, Tuple[StopPlace, Quay]]:
        if self.scheduled_stop_point_ref_to_physical is None:
            self.scheduled_stop_point_ref_to_physical = {}
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


    def get_service_journey_service_journey_pattern_group(self):
        if self.service_journey_service_journey_pattern_group is None:
            service_journeys = list(self.get_service_journeys().values())
            service_journeys.sort(key = operator.attrgetter('journey_pattern_ref.ref', '_departure_time_seconds'))
            service_journey_service_journey_pattern_group = {k: list(v) for k, v in groupby(service_journeys, operator.attrgetter('journey_pattern_ref.ref'))}

            _jp_idx = 0
            for journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
                _jpvjoffset = 0
                for service_journey in service_journeys:
                    service_journey._jp_idx = _jp_idx
                    service_journey._jpvjoffset = _jpvjoffset
                    _jpvjoffset += 1

                _jp_idx += 1

            self.service_journey_service_journey_pattern_group = service_journey_service_journey_pattern_group

        return self.service_journey_service_journey_pattern_group

    def get_type_of_productcategories(self) -> Dict[str, TypeOfProductCategory]:
        if self.type_of_productcategories is None:
            self.type_of_productcategories = collections.OrderedDict({x.id: x for x in [self.parser.parse(element, TypeOfProductCategory) for element in self.tree.findall(".//{http://www.netex.org.uk/netex}TypeOfProductCategory")]})

        return self.type_of_productcategories

class Index2:
    parser: XmlParser
    tree: etree._ElementTree
    writer: Writer

    n_stops: int
    loc_stop_point_coords: int

    loc_for_string: dict
    strings: List[str]
    string_length: int

    netex_timetable: NeTExTimetable

    global_utc_offset: int

    """
    def put_string(self,string):
        if string in self.loc_for_string:
            return self.loc_for_string[string]
        self.loc_for_string[string] = self.string_length
        self.string_length += (len(string) + 1)
        self.strings.append(string)

        return self.loc_for_string[string]
    """

    def write_stop_point_idx(self, scheduled_stop_point_ref: str):
        if self.n_stops <= 65535:
            self.out.writeshort(list(self.netex_timetable.scheduled_stop_points.keys()).index(scheduled_stop_point_ref))
        else:
            self.out.writeint(list(self.netex_timetable.scheduled_stop_points.keys()).index(scheduled_stop_point_ref))

    def write_stop_area_idx(self, stop_place_ref: str):
        if self.n_stops <= 65535:
            self.out.writeshort(list(self.netex_timetable.stop_places.keys()).index(stop_place_ref))
        else:
            self.out.writeint(list(self.netex_timetable.stop_places.keys()).index(stop_place_ref))

    def write_list_of_strings(self, list_of_strings: List[str]):
        loc = self.out.tell()
        for x in list_of_strings:
            self.out.writeint(self.out.put_string(x or ''))
        return loc

    def __init__(self, netex_timetable: NeTExTimetable, out):

        self.out = out
        self.n_stops = 0
        self.loc_stop_point_coords = 0

        self.loc_for_string = {}
        self.strings = []
        self.string_length = 0
        self.global_utc_offset = 0

        self.netex_timetable = netex_timetable

    def export_sp_coords(self):
        self.out.write_text_comment("STOP POINT COORDS")
        self.loc_stop_point_coords = self.out.tell()

        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            self.out.write2floats(scheduled_stop_point.location.latitude or 0.0, scheduled_stop_point.location.longitude or 0.0)
            self.n_stops += 1

    def export_sp_names(self):
        self.out.write_text_comment("STOP POINT NAMES")

        stop_names = [scheduled_stop_point.name.value for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_nameidx = self.write_list_of_strings(stop_names)

    def export_sp_uris(self):
        # stopid index was several times bigger than the string table. it's probably better to just store fixed-width ids.
        self.out.write_text_comment("STOP_POINT IDS")
        stop_ids = [scheduled_stop_point.id for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values()]
        self.loc_stop_point_uris = self.write_list_of_strings(stop_ids)

    def export_sp_attributes(self):
        self.out.write_text_comment("STOP POINT ATTRIBUTES")
        self.loc_stop_point_attributes = self.out.tell()

        scheduled_stop_points = self.netex_timetable.get_scheduled_stop_points()
        scheduled_stop_point_ref_to_physical = self.netex_timetable.get_scheduled_stop_point_ref_to_physical()
        parkings = self.netex_timetable.get_parkings()

        for scheduled_stop_point in scheduled_stop_points.values():
            quay: Quay
            stop_place: StopPlace

            quay, stop_place = scheduled_stop_point_ref_to_physical[scheduled_stop_point.id]
            accessibility_assessment = stop_place.accessibility_assessment
            place_equipments = stop_place.place_equipments
            if quay is not None:
                accessibility_assessment = quay.accessibility_assessment
                place_equipments = quay.place_equipments

            stop_attribute = 0

            if accessibility_assessment is not None and accessibility_assessment.suitabilities is not None:
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

            self.out.writebyte(stop_attribute)

    def export_journey_pattern_point_stop(self):
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()

        self.out.write_text_comment("JOURNEY PATTERN POINT STOP")
        self.loc_journey_pattern_points = self.out.tell()
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

        self.out.write_text_comment("JOURNEY PATTERN POINT ATTRIBUTES")
        self.loc_journey_pattern_point_attributes = self.out.tell()
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
                self.out.writebyte(attr)
                offset += 1

    def export_journey_pattern_point_headsigns(self):
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()
        # destination_displays = self.netex_timetable.get_destination_displays()

        self.out.write_text_comment("JOURNEY PATTERN POINT HEADSIGN")
        self.loc_journey_pattern_point_headsigns = self.out.tell()
        self.offset_jpp = []
        offset = 0
        for service_journey_pattern in service_journey_patterns.values():
            self.offset_jpp.append(offset)
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                self.out.writeint(self.out.put_string(point_in_sequence.destination_display_ref_or_destination_display_view.front_text.value))
                offset += 1

    @staticmethod
    def to_seconds(xml_time: XmlTime, day_offset: int = 0):
        _time = xml_time.to_time()
        return ((day_offset or 0) * 24 + (_time.hour or 0)) * 3600 + (_time.minute or 0) * 60 + (_time.second or 0)

    @staticmethod
    def to_seconds2(xml_duration: XmlDuration):
        return ((xml_duration.days or 0) * 24 + (xml_duration.hours or 0)) * 3600 + (xml_duration.minutes or 0) * 60 + (xml_duration.seconds or 0)


    def export_timedemandtypes(self):
        # This is the only structure we actually will do pre-processing on.
        # Our TimeDemandType consists from relative times, each from the first departure time.
        # This is different from how NeTEx models it, since it uses relative distances between stops (on TimingLinks)
        # and uses points for wait times.

        service_journeys = self.netex_timetable.get_service_journeys()

        tentative: List[tuple] = []
        sj_to_tdt: Dict[str, int]
        self.sj_to_tdt = {}

        for service_journey in service_journeys.values():
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

                relative_distances.append((current_arrival_time - first_departure_time, current_departure_time - first_departure_time,))

            _tuple = tuple(relative_distances)
            if _tuple not in tentative:
                tentative.append(_tuple)

            self.sj_to_tdt[service_journey.id] = tentative.index(_tuple)

        self.out.write_text_comment("TIME DEMAND TYPES")
        self.loc_timedemandgroups = self.out.tell()
        self.offset_for_timedemandgroup_uri: Dict[int, int] = {}
        tp_offset = 0
        for i in range(0, len(tentative)):
            self.offset_for_timedemandgroup_uri[i] = tp_offset
            for tpp in tentative[i]:
                # TODO must write
                self.out.write_timedemandgroup(tpp[0] >> 2, tpp[1] >> 2)
                tp_offset += 1
        self.n_tpp = tp_offset

    @staticmethod
    def get_service_journey(service_journey: ServiceJourney) -> (int, int):
        departure_time = Index2.to_seconds(service_journey.passing_times.timetabled_passing_time[0].departure_time, service_journey.passing_times.timetabled_passing_time[0].departure_day_offset)
        vj_attr = 0

        if service_journey.transport_submode is not None and isinstance(service_journey.transport_submode.choice, BusSubmode):
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
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()

        self.out.write_text_comment("VEHICLE JOURNEYS USING JOURNEY_PATTERN")
        self.loc_vehicle_journeys = self.out.tell()
        tioffset = 0
        self.vj_ids_offsets = []
        for service_journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
            self.vj_ids_offsets.append(tioffset)
            for service_journey in service_journeys:
                departure_time, vj_attr = Index2.get_service_journey(service_journey)
                # TODO
                # assert (tioffset - index.vj_ids_offsets[vj._jp_idx]) == vj._jpvjoffset
                self.out.write_vj(self.offset_for_timedemandgroup_uri[self.sj_to_tdt[service_journey.id]],
                                         (departure_time + self.global_utc_offset) >> 2, vj_attr)
                tioffset += 1

    def export_jpp_at_sp(self):
        journey_patterns_at_stop_point = {}
        service_journey_patterns: List[ServiceJourneyPattern] = list(self.netex_timetable.get_service_journey_patterns().values())
        for service_journey_pattern in service_journey_patterns:
            for point_in_sequence in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                _set = journey_patterns_at_stop_point.get(point_in_sequence.scheduled_stop_point_ref.ref, set([]))
                _set.add(service_journey_pattern.id)
                journey_patterns_at_stop_point[point_in_sequence.scheduled_stop_point_ref.ref] = _set

        service_journey_patterns_idx = [service_journey_pattern.id for service_journey_pattern in service_journey_patterns]

        self.out.write_text_comment("JOURNEY_PATTERNS AT STOP")
        self.loc_jp_at_sp = self.out.tell()
        self.jpp_at_sp_offsets = []
        n_offset = 0
        for scheduled_stop_point in self.netex_timetable.scheduled_stop_points.values():
            journey_pattern_refs = journey_patterns_at_stop_point[scheduled_stop_point.id]
            self.jpp_at_sp_offsets.append(n_offset)
            for journey_pattern_ref in journey_pattern_refs:
                self.out.writeshort(service_journey_patterns_idx.index(journey_pattern_ref))
                n_offset += 1
        self.jpp_at_sp_offsets.append(n_offset) #sentinel
        self.n_jpp_at_sp = n_offset

    def export_transfers(self):
        # passenger_stop_assignments = self.netex_timetable.get_passenger_stop_assignments()
        # passenger_stop_assignments.sort(key=operator.attrgetter('taxi_stand_ref_or_quay_ref_or_quay.ref'))
        # passenger_stop_assignments_by_quay_ref = groupby(passenger_stop_assignments, operator.attrgetter('taxi_stand_ref_or_quay_ref_or_quay.ref'))

        # path_links2 = []
        # path_links = self.netex_timetable.get_path_links()
        # for path_link in path_links:
        #    for _from in passenger_stop_assignments_by_quay_ref.get(path_link.from_value.place_ref.ref, []):
        #        for _to in passenger_stop_assignments_by_quay_ref.get(path_link.to.place_ref.ref, []):
        #            path_links2.append((_from, _to, Index2.to_seconds2(path_link.transfer_duration.default_duration)))

        # path_links2.sort(key=operator.itemgetter(1))
        # path_links_by_scheduled_stop_point_ref = groupby(path_links2, operator.itemgetter(1))

        connections = self.netex_timetable.get_connections()
        connections.sort(key=operator.attrgetter('from_value.scheduled_stop_point_ref_or_vehicle_meeting_point_ref.ref'))
        connections_by_scheduled_stop_point_ref: Dict[str, Iterable[Connection]] = {
            k: list(v) for k, v in groupby(connections, operator.attrgetter('from_value.scheduled_stop_point_ref_or_vehicle_meeting_point_ref.ref'))
        }

        print("saving transfer stops (footpaths)")
        self.out.write_text_comment("TRANSFER TARGET STOPS")
        self.loc_transfer_target_stop_points = self.out.tell()

        self.transfers_offsets = []
        offset = 0
        transfertimes = []
        stop_point_waittimes = {}
        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            self.transfers_offsets.append(offset)
            if scheduled_stop_point.id not in connections_by_scheduled_stop_point_ref:
                continue
            for connection in connections_by_scheduled_stop_point_ref[scheduled_stop_point.id]:
                _from = connection.from_value.scheduled_stop_point_ref_or_vehicle_meeting_point_ref.ref
                _to = connection.to.scheduled_stop_point_ref_or_vehicle_meeting_point_ref.ref
                _default_duration = Index2.to_seconds2(connection.transfer_duration.default_duration)
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
        self.out.write_text_comment("TRANSFER TIMES")
        self.loc_transfer_dist_meters = self.out.tell()

        for transfer_time in transfertimes:
            self.out.writeshort((int(transfer_time) >> 2))

        self.out.write_text_comment("MIN WAIT TIMES")
        self.loc_stop_point_waittime = self.out.tell()
        for scheduled_stop_point in self.netex_timetable.get_scheduled_stop_points().values():
            _wait_time = stop_point_waittimes.get(scheduled_stop_point.id, MIN_WAITTIME)
            self.out.writeshort((int(_wait_time) >> 2))

    def export_vj_interlines(self):
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()
        service_journey_interchanges = self.netex_timetable.get_service_journey_interchanges()
        service_journeys = self.netex_timetable.get_service_journeys()

        vj_interline_clockwise = {}
        vj_interline_counterclockwise = {}

        for service_journey_interchange in service_journey_interchanges:
            _from = service_journey_interchange.from_journey_ref.ref
            _to = service_journey_interchange.to_journey_ref.ref

            from_vj = service_journeys[_from]
            to_vj = service_journeys[_to]

            _arrival_time = Index2.to_seconds(from_vj.passing_times.timetabled_passing_time[-1].arrival_time, from_vj.passing_times.timetabled_passing_time[-1].arrival_day_offset)
            _departure_time = Index2.to_seconds(to_vj.passing_times.timetabled_passing_time[0].departure_time, to_vj.passing_times.timetabled_passing_time[0].departure_day_offset)

            if _arrival_time > _departure_time:
                print(f'Ignoring VJ interline {service_journey_interchange.id} from {from_vj.id} to {to_vj.id}, timetravel!')
                continue

            waittime = _arrival_time - _departure_time
            if waittime > MAX_INTERLINE_WAITTIME:
                print(f'Ignoring VJ interline {service_journey_interchange.id} from {from_vj.id} to {to_vj.id}, wait-time between VJs is {waittime} seconds!')
                continue

            if (from_vj._utc_offset, from_vj.id) in vj_interline_clockwise:
                raise Exception("Vehicle_journey's can only point to ONE other VJ")

            vj_interline_clockwise[(from_vj._utc_offset, from_vj.id)] = (to_vj._jp_idx, to_vj._jpvjoffset)

            if (to_vj._utc_offset, to_vj.id) in vj_interline_counterclockwise:
                raise Exception("Vehicle_journey's can only point to ONE other VJ counterclockwise")

            vj_interline_counterclockwise[(to_vj._utc_offset, to_vj.id)] = (from_vj._jp_idx, from_vj._jpvjoffset)

        self.out.write_text_comment("INTERLINE BACKWARD")
        self.loc_vj_interline_backward = self.out.tell()
        n_vjtransfers = 0

        for service_journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
            for service_journey in service_journeys:
                _key = (service_journey._utc_offset, service_journey.id) # TODO: we don't have a utc_offset
                _interline = vj_interline_counterclockwise.get(_key, None)
                if _interline:
                    self.out.write_vjref(*_interline)
                else:
                    self.out.write_vjref(JP_NONE,VJ_NONE)
                n_vjtransfers += 1

        self.out.write_text_comment("INTERLINE FORWARD")
        self.loc_vj_interline_forward = self.out.tell()
        n_vjtransfers_forward = 0

        for service_journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
            for service_journey in service_journeys:
                _key = (service_journey._utc_offset, service_journey.id)  # TODO: we don't have a utc_offset
                _interline = vj_interline_clockwise.get(_key, None)
                if _interline:
                    self.out.write_vjref(*_interline)
                else:
                    self.out.write_vjref(JP_NONE,VJ_NONE)
                n_vjtransfers_forward += 1
        assert n_vjtransfers == n_vjtransfers_forward

    def export_stop_indices(self):
        print("saving stop indexes")
        self.out.write_text_comment("STOP STRUCTS")
        self.loc_stop_points = self.out.tell()
        print(len(self.jpp_at_sp_offsets), len(self.transfers_offsets))
        assert len(self.jpp_at_sp_offsets) == len(self.transfers_offsets)
        for stop in zip (self.jpp_at_sp_offsets, self.transfers_offsets):
            self.out.write_stopstruct(*stop)

    @staticmethod
    def map_transport_mode(transport_mode: AllVehicleModesOfTransportEnumeration):
        mode = 0
        match transport_mode:
            case AllVehicleModesOfTransportEnumeration.TRAM:
                return 1
            case AllVehicleModesOfTransportEnumeration.METRO:
                return 2
            case AllVehicleModesOfTransportEnumeration.RAIL:
                return 4
            case AllVehicleModesOfTransportEnumeration.BUS:
                return 8
            case AllVehicleModesOfTransportEnumeration.FERRY:
                return 16
            case AllVehicleModesOfTransportEnumeration.CABLEWAY:
                return 32
            # TODO: Gondola
            case AllVehicleModesOfTransportEnumeration.FUNICULAR:
                return 128
            case AllVehicleModesOfTransportEnumeration.ALL:
                return 255
            case _:
                return 0

    def export_jp_structs(self):
        lines = self.netex_timetable.get_lines()
        routes = self.netex_timetable.get_routes()
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()

        routeref_to_lineref = {route.id : route.line_ref.ref for route in routes.values()}

        r_idx = list(routes.keys())

        self.out.write_text_comment("ROUTE STRUCTS")
        self.loc_journey_patterns = self.out.tell()
        jpp_offsets = self.offset_jpp
        trip_ids_offsets = self.vj_ids_offsets
        jp_attributes = []

        nroutes = len(service_journey_patterns)

        jp_n_jpp = []
        jp_n_vj = []
        routeidx_offsets = []
        jp_min_time = []
        jp_max_time = []
        for service_journey_pattern in service_journey_patterns.values():
            jp_n_jpp.append(len(service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern))
            jp_n_vj.append(len(service_journey_service_journey_pattern_group[service_journey_pattern.id]))

            # TODO: it feels like this is wrong, the vj.utc_offset is not considered.
            jp_min_time.append(min([service_journey._departure_time_seconds + self.global_utc_offset for service_journey in service_journey_service_journey_pattern_group[service_journey_pattern.id]]) >> 2)
            jp_max_time.append(max([service_journey._arrival_time_seconds + self.global_utc_offset for service_journey in service_journey_service_journey_pattern_group[service_journey_pattern.id]]) >> 2)
            routeidx_offsets.append(r_idx.index(service_journey_pattern.route_ref_or_route_view.ref))

            _line = lines[routeref_to_lineref[service_journey_pattern.route_ref_or_route_view.ref]]
            jp_attributes.append(self.map_transport_mode(_line.transport_mode))

        jp_t_fields = [jpp_offsets, trip_ids_offsets, jp_n_jpp, jp_n_vj, jp_attributes, routeidx_offsets, jp_min_time, jp_max_time]
        for l in jp_t_fields:
            # the extra last route is a sentinel so we can derive list lengths for the last true route.
            assert len(l) == nroutes
        for route in zip (*jp_t_fields) :
            # print route
            self.out.write_route(*route)
        self.out.write_route(jpp_offsets[-1]+1, 0, 0, 0, 0, 0, 0, 0) #Sentinel

    @staticmethod
    def validity_mask(valid_day_bits):
        mask = 0
        for day in range(0, min(NUMBER_OF_DAYS, len(valid_day_bits))):
            mask |= 1 << day
        return mask

    def export_vj_validities(self):
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()

        print("writing bitfields indicating which days each trip is active")
        # note that bitfields are ordered identically to the trip_ids table, and offsets into that table can be reused
        self.out.write_text_comment("VJ ACTIVE BITFIELDS")
        self.loc_vj_active = self.out.tell()

        for service_journey_pattern, service_journeys in service_journey_service_journey_pattern_group.items():
            for service_journey in service_journeys:
                service_journey: ServiceJourney
                availability_condition: AvailabilityCondition = service_journey.validity_conditions_or_valid_between[0].choice[0]
                self.out.writeint(Index2.validity_mask(availability_condition.valid_day_bits))

    def export_jp_validities(self):
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()

        print("writing bitfields indicating which days each trip is active")
        # note that bitfields are ordered identically to the trip_ids table, and offsets into that table can be reused
        self.out.write_text_comment("JP ACTIVE BITFIELDS")
        self.loc_jp_active = self.out.tell()
        n_zeros = 0
        for service_journey_pattern_ref, _vjs in service_journey_service_journey_pattern_group.items():
            availability_condition: AvailabilityCondition = service_journey_patterns[service_journey_pattern_ref].validity_conditions_or_valid_between[0].choice[0]
            self.out.writeint(Index2.validity_mask(availability_condition.valid_day_bits))

    def export_platform_codes(self):
        scheduled_stop_points = self.netex_timetable.get_scheduled_stop_points()
        print("writing out platformcodes for stops")
        self.out.write_text_comment("PLATFORM CODES")

        platform_codes = []
        for ssp in self.netex_timetable.get_scheduled_stop_points().values():
            if ssp.public_code is not None:
                platform_codes.append(ssp.public_code.value)
            else:
                platform_codes.append('')

        # Check ift
        self.loc_platformcodes = self.write_list_of_strings(platform_codes)

    def export_sa_coords(self):
        stop_places = self.netex_timetable.get_stop_places()

        self.out.write_text_comment("STOP AREA COORDS")
        self.loc_stop_area_coords = self.out.tell()
        for sp in stop_places.values():
            self.out.write2floats(sp.centroid.location.latitude or 0.0, sp.centroid.location.longitude or 0.0)

    def export_sa_for_sp(self):
        scheduled_stop_points = self.netex_timetable.get_scheduled_stop_points()
        scheduled_stop_point_ref_to_physical = self.netex_timetable.get_scheduled_stop_point_ref_to_physical()

        self.out.write_text_comment("STOP_POINT -> STOP_AREA")
        self.loc_sa_for_sp = self.out.tell()

        for scheduled_stop_point in scheduled_stop_points.values():
            quay: Quay
            stop_place: StopPlace

            _quay, stop_place = scheduled_stop_point_ref_to_physical[scheduled_stop_point.id]
            self.write_stop_area_idx(stop_place.id)

    def export_sa_names(self):
        self.out.write_text_comment("STOP AREA NAMES")

        stop_area_names = [stop_place.name.value for stop_place in self.netex_timetable.get_stop_places().values()]
        self.loc_stop_areaidx = self.write_list_of_strings(stop_area_names)

    def export_operators(self):
        operators = self.netex_timetable.get_operators()

        print("writing out opreators to string pool")
        self.out.write_text_comment("OPERATOR IDS")
        self.loc_operator_ids = self.write_list_of_strings([op.id for op in operators.values()])
        self.out.write_text_comment("OPERATOR NAMES")
        self.loc_operator_names = self.write_list_of_strings([op.name.value for op in operators.values()])
        self.out.write_text_comment("OPERATOR URLS")
        self.loc_operator_urls = self.write_list_of_strings([op.contact_details.url or '' for op in operators.values()])

    # TODO: rrrr stores a commercial mode per JourneyPattern
    def export_commercialmodes(self):
        routes = self.netex_timetable.get_routes()
        lines = self.netex_timetable.get_lines()
        commercial_modes = self.netex_timetable.get_type_of_productcategories()
        service_journey_patterns = self.netex_timetable.get_service_journey_patterns()

        print("writing out commercial_mode to string table")
        self.out.write_text_comment("CCMODE IDS")
        self.loc_commercialmode_ids = self.write_list_of_strings([cc.id for cc in commercial_modes.values()])
        self.out.write_text_comment("CCMODE NAMES")
        self.loc_commercialmode_names = self.write_list_of_strings([cc.name.value for cc in commercial_modes.values()])

        self.out.write_text_comment("COMMERCIAL MODE FOR JOURNEY PATTERN")
        self.loc_commercial_mode_for_jp = self.out.tell()

        routeref_to_lineref = {route.id : route.line_ref.ref for route in routes.values()}

        cc_idx = list(commercial_modes.keys())
        for sjp in service_journey_patterns.values():
            line: Line = lines[routeref_to_lineref[sjp.route_ref_or_route_view.ref]]
            self.out.writeshort(cc_idx.index(line.type_of_product_category_ref.ref))

    # TODO: Review
    def export_physicalmodes(self):
        lines = self.netex_timetable.get_lines()
        # vehicle_types = self.netex_timetable.get_vehicle_types()
        type_of_productcategories = self.netex_timetable.get_type_of_productcategories()

        print("writing out physical_mode to string table")
        self.out.write_text_comment("PHYSICAL MODE IDS")
        self.loc_physicalmode_ids = self.write_list_of_strings([pc.id for pc in type_of_productcategories.values()])
        self.out.write_text_comment("PHYSICAL MODE NAMES")
        self.loc_physicalmode_names = self.write_list_of_strings([pc.name.value for pc in type_of_productcategories.values()])
        self.loc_physical_mode_for_line = self.out.tell()

        self.out.write_text_comment("PHYSICAL MODE FOR LINE")
        pc_idx = list(type_of_productcategories.keys())
        for l in lines.values():
            self.out.writeshort(pc_idx.index(l.type_of_product_category_ref.ref))

    def export_line_for_route(self):
        routes = self.netex_timetable.get_routes()
        lines = self.netex_timetable.get_lines()

        l_idx = list(lines.keys())

        self.out.write_text_comment("LINE FOR ROUTE")
        self.loc_line_for_route = self.out.tell()
        for r in routes.values():
            self.out.writeshort(l_idx.index(r.line_ref.ref))

    @staticmethod
    def get_colour_or_empty(presentation: PresentationStructure, attr: str):
        if presentation is not None:
            colour = getattr(presentation, attr)
            if colour is not None:
                return colour.hex()

        return ''

    def export_line_attributes(self):
        print("Writing line attributes")

        lines = self.netex_timetable.get_lines()
        operators = self.netex_timetable.get_operators()

        o_idx = list(operators.keys())

        # TODO assert that len(o_idx) <= 255 (less or equal than 255 operators)

        self.out.write_text_comment("OPERATOR FOR LINE")
        self.loc_operator_for_line = self.out.tell()
        for l in lines.values():
            self.out.writebyte(o_idx.index(l.operator_ref.ref))

        self.out.write_text_comment("LINE CODES")
        self.loc_line_codes = self.write_list_of_strings([line.public_code.value or '' for line in lines.values()])

        self.out.write_text_comment("LINE COLOR")
        self.loc_line_color = self.write_list_of_strings([self.get_colour_or_empty(line.presentation, 'colour') for line in lines.values()])

        self.out.write_text_comment("LINE COLOR_TEXT")
        self.loc_line_color_text = self.write_list_of_strings([self.get_colour_or_empty(line.presentation, 'text_colour') for line in lines.values()])

        self.out.write_text_comment("LINE NAMES")
        self.loc_line_names = self.write_list_of_strings([line.name.value or '' for line in lines.values()])

        self.out.write_text_comment("LINE IDS")
        self.loc_line_uris = self.write_list_of_strings([line.id for line in lines.values()])

    def export_sa_attributes(self):
        print("Writing StopPlace attributes")

        stop_places = self.netex_timetable.get_stop_places()

        self.out.write_text_comment("STOP_AREA IDS")
        self.loc_stop_area_uris = self.write_list_of_strings([sa.id for sa in stop_places.values()])

        self.out.write_text_comment("STOP_AREA TIMEZONES")
        self.loc_stop_area_timezones = self.write_list_of_strings([sa.locale.time_zone for sa in stop_places.values()])


    # TODO: Rework
    def export_vj_time_offsets(self):
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()

        print('Timetable offset from UTC {index.global_utc_offset}')
        self.loc_vj_time_offsets = self.out.tell()

        self.out.write_text_comment("VJ OFFSET")

        for service_journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
            for service_journey in service_journeys:
                self.out.writesignedbyte(int((self.global_utc_offset - service_journey._utc_offset) / 60 / 15))  # n * 15 minutes

    def export_vj_uris(self):
        service_journey_service_journey_pattern_group = self.netex_timetable.get_service_journey_service_journey_pattern_group()

        all_vj_ids = []
        for service_journey_pattern_ref, service_journeys in service_journey_service_journey_pattern_group.items():
            for service_journey in service_journeys:
                all_vj_ids.append(service_journey.id)

        print("writing trip ids to string table")
        # note that trip_ids are ordered by departure time within trip bundles (routes), which are themselves in arbitrary order.
        self.out.write_text_comment("VJ IDS")
        self.loc_vj_uris = self.write_list_of_strings(all_vj_ids)
        self.n_vj = len(all_vj_ids)

    def export_stringpool(self):
        print("writing out stringpool")
        self.out.write_text_comment("STRINGPOOL")
        self.loc_stringpool = self.out.tell()
        written_length = 0
        for string in self.out.strings.keys():
            self.out.write_string(string)
            written_length += len(string) + 1
        # assert written_length == self.string_length

    def export(self):
        self.export_sp_coords()
        self.export_journey_pattern_point_stop()
        self.export_journey_pattern_point_attributes()
        self.export_timedemandtypes()
        self.export_vj_in_jp()
        self.export_jpp_at_sp()
        self.export_transfers()
        self.export_vj_interlines()
        self.export_stop_indices()
        self.export_sp_attributes()
        self.export_jp_structs()
        self.export_vj_validities()
        self.export_jp_validities()
        self.export_platform_codes()
        self.export_sa_coords()
        self.export_sa_for_sp()
        self.export_sp_names()
        self.export_sa_names()
        self.export_operators()
        self.export_commercialmodes()
        self.export_physicalmodes()
        self.export_line_for_route()
        self.export_line_attributes()
        self.export_journey_pattern_point_headsigns()
        self.export_sp_uris()
        self.export_sa_attributes()
        self.export_vj_time_offsets()
        self.export_vj_uris()
        self.export_stringpool()
        self.out.write_text_comment("END TTABLEV4")
        index.loc_eof = self.out.tell()
        self.out.write_header()

netex_timetable = NeTExTimetable("/tmp/timetable4.xml")
jw = JSONWriter("/tmp/timetable4.json")
index = Index2(netex_timetable, jw)
index.export()
jw.save()

bw = BinaryWriter("/tmp/timetable4.dat")
index = Index2(netex_timetable, bw)
index.export()
bw.save()