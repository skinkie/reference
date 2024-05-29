import sqlite3
from decimal import Decimal, ROUND_HALF_UP
from functools import partial
from itertools import chain
from typing import List, Iterable, T, Generator

from pyproj import Transformer, CRS
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from anyintodbnew import setup_database, get_interesting_classes
from callsprofile import CallsProfile
from netex import ServiceJourneyPattern, Direction, Codespace, MultilingualString, DirectionType, ServiceJourney, \
    AvailabilityCondition, TimeDemandType, ScheduledStopPoint, Pos, PointVersionStructure, RoutePoint, RouteLink, \
    StopPointInJourneyPattern, TimingPointInJourneyPattern, ScheduledStopPointRef, TimingLink, ServiceLink, \
    TimingLinkRefStructure, ServiceLinkRefStructure, RouteRef, Route, RouteLinkRef, RouteLinkRefStructure, \
    RouteRefStructure, ScheduledStopPointRefStructure, RoutePointRef, RoutePointRefStructure, PointProjection, \
    TimingPoint, TimingPointRefStructure, LineString, Link, LinkVersionStructure, PosList, Line, StopPlace, AccessSpace, \
    Quay, Polygon, PassengerStopAssignment, QuayRefStructure, StopPlaceRefStructure, Block, ServiceJourneyRef, \
    VehicleTypeRef, VersionOfObjectRefStructure, ServiceJourneyPatternRef, LineRef

from refs import getId, getRef, getIndex
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile
from utils import project
from multiprocess import Pool, freeze_support

def ref_version_hash(self):
    return hash(self.ref + ';' + self.version)

VersionOfObjectRefStructure.__hash__ = ref_version_hash
ServiceJourneyRef.__hash__ = ref_version_hash
ServiceJourneyPatternRef.__hash__ = ref_version_hash

def id_version_hash(self):
    return hash(self.id + ';' + self.version)

ServiceJourney.__hash__ = id_version_hash
ServiceJourneyPattern.__hash__ = id_version_hash

# First monkey patching test
def get_route(self, con) -> Route:
    return get_single(con, Route, self.ref, self.version)

RouteRefStructure.get = get_route

def get_routelink(self, con) -> RouteLink:
    return get_single(con, RouteLink, self.ref, self.version)

RouteLinkRefStructure.get = get_routelink

def get_scheduledstoppoint(self, con) -> ScheduledStopPoint:
    return get_single(con, ScheduledStopPoint, self.ref, self.version)

ScheduledStopPointRefStructure.get = get_scheduledstoppoint

def get_quay(self, con) -> Quay:
    return get_single(con, Quay, self.ref, self.version)

QuayRefStructure.get = get_quay

def get_stopplace(self, con) -> StopPlace:
    return get_single(con, StopPlace, self.ref, self.version)

StopPlaceRefStructure.get = get_stopplace


def get_timingpoint(self, con) -> TimingPoint | ScheduledStopPoint:
    if self.name_of_ref_class == 'TimingPoint':
        return get_single(con, TimingPoint, self.ref, self.version)
    elif  self.name_of_ref_class == 'ScheduledStopPoint':
        return get_single(con, ScheduledStopPoint, self.ref, self.version)
    else:
        timing_point = get_single(con, TimingPoint, self.ref, self.version)
        if timing_point is not None:
            return timing_point
        else:
            return get_single(con, ScheduledStopPoint, self.ref, self.version)

TimingPointRefStructure.get = get_timingpoint

def get_servicelink(self, con) -> ServiceLink:
    return get_single(con, ServiceLink, self.ref, self.version)

ServiceLinkRefStructure.get = get_servicelink

def get_timinglink(self, con) -> TimingLink:
    return get_single(con, TimingLink, self.ref, self.version)

TimingLinkRefStructure.get = get_timinglink


ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

transformers = {}

def write_objects(con, objs, empty=False, many=False):
    cur = con.cursor()
    clazz = objs[0].__class__
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    if many:
        print(objectname, len(objs))
        if hasattr(clazz, 'version'):
            cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', [(obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')) for obj in objs])
        else:
            cur.executemany(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);',
                            [(obj.id, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')) for obj in objs])
    else:
        for i in range(0, len(objs)):
            obj = objs[i]
            if hasattr(clazz, 'version'):
                cur.execute(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', (obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')))
            else:
                cur.execute(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);', (obj.id, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')))

            if i % 13 == 0:
                print('\r', objectname, str(i), end = '')
        print('\r', objectname, len(objs), end='')


def write_generator(con, clazz, generator: Generator, empty=False):
    cur = con.cursor()
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    if hasattr(clazz, 'version'):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    else:
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id));"

    cur.execute(sql_create_table)

    def _prepare4(generator4, objectname):
        i = 0
        for obj in generator4:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, obj.order, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')
        print('\r', objectname, i, end='')

    def _prepare3(generator3, objectname):
        i = 0
        for obj in generator3:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')
        print('\r', objectname, i, end='')

    def _prepare2(generator2, objectname):
        i = 0
        for obj in generator2:
            if i % 13 == 0:
                print('\r', objectname, str(i), end='')
            i += 1
            yield obj.id, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')
        print('\r', objectname, i, end='')

    if hasattr(clazz, 'order'):
        cur.executemany(f'INSERT INTO {objectname} (id, version, ordr, object) VALUES (?, ?, ?, ?);', _prepare4(generator, objectname))
    elif hasattr(clazz, 'version'):
        cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', _prepare3(generator, objectname))
    else:
        cur.execute(f'INSERT INTO {objectname} (id, object) VALUES (?, ?);', _prepare2(generator, objectname))

def infer_directions_from_sjps_and_apply(con, service_journey_patterns: Iterable[ServiceJourneyPattern], generator_defaults):
    used_direction_types = {sjp.direction_type for sjp in service_journey_patterns if sjp.direction_type is not None}
    directions = {}
    for used_direction_type in used_direction_types:
        direction: Direction = Direction(id=getId(Direction, generator_defaults['codespace'], used_direction_type.value),
                                         version=generator_defaults['version'],
                                         name=MultilingualString(value=str(used_direction_type.value)),
                                         direction_type=DirectionType(value=used_direction_type))
        directions[used_direction_type] = direction

    write_objects(con, list(directions.values()), True)

    for sjp in service_journey_patterns:
        sjp.direction_ref_or_direction_view = getRef(directions.get(sjp.direction_type, None))


def project_location2(transformer, location):
    if transformer.target_crs.to_epsg() == 4326:
        if location.pos is not None:
            latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
            location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
            location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
            location.pos = None
    else:
        if location.latitude is not None and location.longitude is not None:
            x, y = transformer.transform(location.longitude, location.latitude)
            location.srs_name = transformer.name
            location.pos = Pos(value=[x, y])
            location.longitude = None
            location.latitude = None
        elif location.pos is not None:
            x, y = transformer.transform(location.pos.value[0], location.pos.value[1])
            location.srs_name = transformer.name
            location.pos = Pos(value=[x, y])

def get_transformer_by_srs_name(location, crs_to) -> Transformer:
    if location.pos is not None:
        srs_name = location.srs_name or location.pos.srs_name or generator_defaults.get('DefaultLocationsystem', 'EPSG:4326')
    else:
        srs_name = location.srs_name or generator_defaults.get('DefaultLocationsystem', 'EPSG:4326')

    if srs_name == crs_to:
        return None

    mapping = f"{srs_name}_{crs_to}"
    transformer = transformers.setdefault(mapping, None)
    if transformer is None:
        transformer = Transformer.from_crs(srs_name, crs_to)
        transformers[mapping] = transformer
    return transformer

def project_location_4326(location, generator_defaults: dict):
    if location.pos is not None:
        transformer = get_transformer_by_srs_name(location, 'urn:ogc:def:crs:EPSG::4326')
        if transformer is not None:
            latitude, longitude = transformer.transform(location.pos.value[0], location.pos.value[1])
        else:
            latitude = location.pos.value[0]
            longitude = location.pos.value[1]

        location.longitude = Decimal(longitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.latitude = Decimal(latitude).quantize(Decimal('0.000001'), ROUND_HALF_UP)
        location.pos = None

    elif location.srs_name not in (None, 'EPSG:4326', 'urn:ogc:def:crs:EPSG::4326') and generator_defaults['DefaultLocationsystem'] not in ('EPSG:4326', 'urn:ogc:def:crs:EPSG::4326'):
        print("TODO: Crazy not WGS84")

def project_location(points: Iterable[PointVersionStructure], generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    if crs_to == 'EPSG:4326':
        for point in points:
            location = None
            if hasattr(point, 'centroid'):
                if point.centroid is not None:
                    location = point.centroid.location
            else:
                location = point.location

            if location is not None and location.srs_name != crs_to:
                project_location_4326(transformer, location)
    else:
        for point in points:
            location = None
            if hasattr(point, 'centroid'):
                if point.centroid is not None:
                    location = point.centroid.location
            else:
                location = point.location

            if location is not None and location.srs_name != crs_to:
                project_location2(transformer, location)



def project_location(points: Iterable[PointVersionStructure], generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    if crs_to == 'EPSG:4326':
        for point in points:
            location = None
            if hasattr(point, 'centroid'):
                if point.centroid is not None:
                    location = point.centroid.location
            else:
                location = point.location

            if location is not None:
                project_location_4326(location, generator_defaults)
    else:
        for point in points:
            location = None
            if hasattr(point, 'centroid'):
                if point.centroid is not None:
                    location = point.centroid.location
            else:
                location = point.location

            if location is not None and location.srs_name is not None and location.srs_name != crs_to:
                project_location2(transformer, location)


def project_linestring2(transformer, linestring):
    srs_dimension = linestring.srs_dimension if hasattr(linestring, 'srs_dimension') and linestring.srs_dimension else 2
    xx = []
    yy = []
    zz = []
    if isinstance(linestring.pos_or_point_property_or_pos_list[0], PosList):
        xx = linestring.pos_or_point_property_or_pos_list[0].value[0::srs_dimension]
        yy = linestring.pos_or_point_property_or_pos_list[0].value[1::srs_dimension]
        if srs_dimension >= 2:
            zz = linestring.pos_or_point_property_or_pos_list[0].value[2::srs_dimension]
    elif isinstance(linestring.pos_or_point_property_or_pos_list[0], Pos):
        xx = [pos.value[0] for pos in linestring.pos_or_point_property_or_pos_list]
        yy = [pos.value[1] for pos in linestring.pos_or_point_property_or_pos_list]
        if srs_dimension >= 2:
            zz = [pos.value[2] for pos in linestring.pos_or_point_property_or_pos_list]

    if srs_dimension == 2:
        pxx, pyy = transformer.transform(xx, yy)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy))))]
    elif srs_dimension == 3:
        pxx, pyy, pzz = transformer.transform(xx, yy, zz)
        linestring.pos_or_point_property_or_pos_list = [PosList(value=list(chain(*zip(pxx, pyy, pzz))))]

def project_linestring(links: Iterable[LinkVersionStructure], generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    for link in links:
        if link.line_string.srs_name != crs_to:
            project_linestring2(transformer, link.line_string)
            if crs_to == 'EPSG:4326':
                link.line_string.pos_or_point_property_or_pos_list[0].value = [Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in link.line_string.pos_or_point_property_or_pos_list[0].value]

def project_polygon(polygon: Polygon, generator_defaults, crs_to):
    transformer = transformers.get(generator_defaults['DefaultLocationsystem'], Transformer.from_crs(generator_defaults['DefaultLocationsystem'], crs_to))
    transformers[generator_defaults['DefaultLocationsystem']] = transformer
    project_linestring2(transformer, polygon.exterior.linear_ring)
    for interior in polygon.interior:
        project_linestring2(transformer, interior)
    if crs_to == 'EPSG:4326':
        polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value = [Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in polygon.exterior.linear_ring.pos_or_point_property_or_pos_list[0].value]
        for interior in polygon.interior:
            interior.linear_ring.pos_or_point_property_or_pos_list[0].value = [
                Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in
                interior.linear_ring.pos_or_point_property_or_pos_list[0].value]

def load_local(con, clazz: T, limit=None) -> List[T]:
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")

    objs: List[T] = []
    for xml, in cur.fetchall():
        obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs

def load_generator(con, clazz, limit=None):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield parser.from_bytes(xml[0], clazz)

def get_single(con, clazz: T, id, version) -> T:
    type = getattr(clazz.Meta, 'name', clazz.__name__)
    cur = con.cursor()
    if version == 'any' or version is None:
        cur.execute(f"SELECT object FROM {type} WHERE id = ? ORDER BY version DESC LIMIT 1;", (id,))
    else:
        cur.execute(f"SELECT object FROM {type} WHERE id = ? AND version = ? LIMIT 1;", (id, version,))

    row = cur.fetchone()
    if row is not None:
        obj = parser.from_bytes(row[0], clazz)
        return obj

def find_route_link(con, from_point: RoutePointRefStructure, to_point: RoutePointRefStructure, route_links: List[RouteLink], offset=0) -> (RouteLink, int):
    if from_point is None or to_point is None:
        return (None, offset)

    for i in range(offset, len(route_links)):
        route_link: RouteLink = route_links[i]
        if route_link.from_point_ref.ref == from_point.ref and route_link.to_point_ref.ref == to_point.ref:
            return (route_link, i)

    return (None, offset)

def point_to_route_point_ref(point):
    if point.projections:
        for projection in point.projections.projection_ref_or_projection:
            if isinstance(projection, PointProjection):
                projection: PointProjection
                if projection.project_to_point_ref is not None and projection.project_to_point_ref.name_of_ref_class == 'RoutePoint':
                    return project(projection.project_to_point_ref, RoutePointRef)

def append_timing_links_to_service_link(con, pis: StopPointInJourneyPattern, intermediate_timing_links: List[TimingLinkRefStructure], scheduled_stop_point_ref: ScheduledStopPointRef, route_links: List[RouteLink], new_service_links: List[ServiceLink], offset):
    service_link: ServiceLink = None
    if pis.onward_timing_link_ref:
        service_link = project(pis.onward_timing_link_ref.get(con), ServiceLink)
        new_service_links.append(service_link)
        pis.onward_service_link_ref = getRef(service_link, ServiceLinkRefStructure)

        # First strategy: we must find a RouteLink that has the FromPoint + ToPoint
        from_ssp: ScheduledStopPoint = service_link.from_point_ref.get(con)
        from_ssp_pp = point_to_route_point_ref(from_ssp)
        to_ssp: ScheduledStopPoint = service_link.to_point_ref.get(con)
        to_ssp_pp = point_to_route_point_ref(to_ssp)

        route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
        if route_link is not None:
            route_link: RouteLink
            service_link.line_string = route_link.line_string
            if len(intermediate_timing_links) > 0:
                service_link.line_string.id += '_extended'

        tl: TimingLink = None
        for tl_ref in intermediate_timing_links:
            tl = tl_ref.get(con)
            # update the previous pis's service link, so the timing links are appended
            # we only care about the line string, nothing else, resolve matching routelink

            from_point = tl.from_point_ref.get(con)
            from_point_pp = point_to_route_point_ref(from_point)
            to_point = tl.to_point_ref.get(con)
            to_point_pp = point_to_route_point_ref(to_point)

            route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
            if route_link is not None:
                route_link: RouteLink
                # TODO: guard for dimensions
                if service_link.line_string[-2:] == route_link.line_string[0:2]:
                    service_link.line_string += route_link.line_string[2:]
                else:
                    print("End does not match start")

        if tl is not None and (
                tl.to_point_ref.name_of_ref_class == 'ScheduledStopPoint' or 'ScheduledStopPoint' in tl.to_point_ref.ref):
            service_link.to_point_ref = project(tl.to_point_ref, ScheduledStopPointRefStructure)

        pis.onward_timing_link_ref = None
    else:
        service_link = pis.onward_service_link_ref.get(con)
        # First strategy: we must find a RouteLink that has the FromPoint + ToPoint
        from_ssp: ScheduledStopPoint = service_link.from_point_ref.get(con)
        from_ssp_pp = point_to_route_point_ref(from_ssp)
        to_ssp: ScheduledStopPoint = service_link.to_point_ref.get(con)
        to_ssp_pp = point_to_route_point_ref(to_ssp)

        route_link, offset = find_route_link(con, from_ssp_pp, to_ssp_pp, route_links, offset + 1)
        if route_link is not None:
            route_link: RouteLink
            service_link.line_string = route_link.line_string

    if service_link.to_point_ref.ref != scheduled_stop_point_ref.ref:
        print("Expected end points don't match.")

    return offset


def transform_timinglinks_to_servicelinks(con, service_journey_pattern: ServiceJourneyPattern):
    route_links: List[RouteLink] = None
    if isinstance(service_journey_pattern.route_ref_or_route_view, RouteRef):
        route: Route = service_journey_pattern.route_ref_or_route_view.get(con)
        route_links = [por.onward_route_link_ref.get(con) for por in route.points_in_sequence.point_on_route if por.onward_route_link_ref is not None]

    # Van de ScheduledStopPoints is er een projectie naar RoutePoint
    # De RouteLink van de Route die hier gebruikt wordt (in volgorde) zou dus een relatie moeten hebben
    # tussen de eerst bekende scheduled stop point en de laatst gevonden scheduled stop point (geprojecteerd naar RoutePoint, als Ref)

    previous_pis = None
    new_pis_sequence = []
    intermediate_timing_links = []
    service_links = []
    offset = -1

    for pis in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
        if isinstance(pis, StopPointInJourneyPattern):
            pis: StopPointInJourneyPattern
            # Handle that the previous pis, with a timing_link, now becomes a service_link
            if previous_pis is not None:
                offset = append_timing_links_to_service_link(con, previous_pis, intermediate_timing_links, pis.scheduled_stop_point_ref, route_links, service_links, offset)

            intermediate_timing_links = []

            new_pis_sequence.append(pis)

            previous_pis = pis

        elif isinstance(pis, TimingPointInJourneyPattern):
            pis: TimingPointInJourneyPattern
            if isinstance(pis.timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref, ScheduledStopPointRef):
                # If this is the case, we must rewrite the TimingPointInSequence as a StopPointInJourneyPattern, otherwise we cannot create a OnwardServiceLink
                new_pis: StopPointInJourneyPattern = project(pis, StopPointInJourneyPattern)
                new_pis.scheduled_stop_point_ref = pis.timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref
                new_pis_sequence.append(new_pis)

                offset = append_timing_links_to_service_link(previous_pis.onward_service_link_ref, intermediate_timing_links, new_pis.scheduled_stop_point_ref, route_links, service_links, offset)
                intermediate_timing_links = []

                previous_pis = new_pis

                # We can directly map the onward_timing_link

            else:
                intermediate_timing_links.append(pis.onward_timing_link_ref)

        if len(intermediate_timing_links):
            # if we end up here, the last pis' refer to timingpoints
            pass

    service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern = new_pis_sequence

    return service_links

import sys

def bison_codespaces(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        codespaces = []
        codespaces.append(Codespace(id="BISON:Codespace:ARR", xmlns_url="http://bison.dova.nu/ns/ARR", xmlns="ARR",
                                    description=MultilingualString(value="Arriva")))
        codespaces.append(Codespace(id="BISON:Codespace:OPENOV", xmlns_url="http://bison.dova.nu/ns/OPENOV", xmlns="OPENOV",
                                    description=MultilingualString(value="openOV")))
        codespaces.append(Codespace(id="BISON:Codespace:CHB", xmlns_url="http://bison.dova.nu/ns/CHB", xmlns="NL:CHB",
                                    description=MultilingualString(value="CHB")))
        write_objects(write_con, codespaces, True, True)


def epip_site_frame_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            refs = set([])

            stop_assignments: List[PassengerStopAssignment] = load_local(read_con, PassengerStopAssignment)
            retain_stop_assignments = []
            for stop_assignment in stop_assignments:
                if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:  # and 'NL:Q:' in stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref:
                    stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref.replace('NL:Q:', 'NL:CHB:Quay:')
                    quay: Quay = stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.get(read_con)
                    if quay is not None:
                        stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.version = quay.version
                        refs.add(quay.id)
                    else:
                        stop_assignment.taxi_stand_ref_or_quay_ref_or_quay = None

                if stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:  # and 'NL:S:' in stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref:
                    stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref.replace('NL:S:', 'NL:CHB:StopPlace:')
                    stop_place: StopPlace = stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.get(read_con)
                    if stop_place is not None:
                        stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.version = stop_place.version
                        refs.add(stop_place.id)
                    else:
                        stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place = None

                if stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None or stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:
                    retain_stop_assignments.append(stop_assignment)

            if len(retain_stop_assignments) > 0:
                write_objects(write_con, retain_stop_assignments, True, True)

            stop_places: List[StopPlace] = load_local(read_con, StopPlace)
            retained_stop_places: List[StopPlace] = []
            for stop_place in stop_places:
                keep = False
                if stop_place.id in refs:
                    keep = True
                else:
                    if stop_place.quays:
                        for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                            if quay.id in refs:
                                keep = True
                                break

                if not keep:
                    continue

                stop_place.equipment_places = None
                if stop_place.access_spaces is not None:
                    for access_space in stop_place.access_spaces.access_space_ref_or_access_space:
                        if isinstance(access_space, AccessSpace):
                            access_space: AccessSpace
                            if access_space.polygon_or_multi_surface:
                                access_space.polygon_or_multi_surface.srsName = "urn:ogc:def:crs:EPSG::4326"
                                access_space.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                    0].value = [
                                    Decimal(value).quantize(Decimal('0.000001'), ROUND_HALF_UP) for value in
                                    access_space.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                        0].value]

                if stop_place.quays:
                    for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                        if isinstance(quay, Quay):
                            quay: Quay
                            if quay.polygon_or_multi_surface:
                                # Reverse order of elements
                                yy = quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                         0].value[0::2]
                                xx = quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list[
                                         0].value[1::2]
                                quay.polygon_or_multi_surface.exterior.linear_ring.pos_or_point_property_or_pos_list = [
                                    PosList(value=list(chain(*zip(xx, yy))))]

                                project_polygon(quay.polygon_or_multi_surface, generator_defaults, 'EPSG:4326')

                            project_location_4326(quay.centroid.location, generator_defaults)

                project_location_4326(stop_place.centroid.location, generator_defaults)
                retained_stop_places.append(stop_place)

            write_objects(write_con, retained_stop_places, True, True)

def epip_route_point_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            route_points = load_local(read_con, RoutePoint )
            project_location(route_points, generator_defaults, 'EPSG:4326')
            write_objects(write_con, route_points, True, True)

def epip_route_link_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            route_links: List[RouteLink] = load_local(read_con, RouteLink)
            for route_link in route_links:
                route_link.line_string = None
                route_link.operational_context_ref = None

            write_objects(write_con, route_links, True, True)

import time

def epip_line_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(line: Line):
        line.branding_ref = None
        line.type_of_service_ref = None
        line.type_of_product_category_ref = None
        return line

    def query(read_database) -> Generator:
        with sqlite3.connect(read_database, check_same_thread=False) as read_con:
            _load_generator = load_generator(read_con, Line)
            for line in pool.imap_unordered(process, _load_generator, chunksize=100):
                yield line

    with sqlite3.connect(write_database) as write_con:
        write_generator(write_con, Line, query(read_database), True)

def epip_line_memory(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            lines: List[Line] = load_local(read_con, Line)
            for line in lines:
                line.branding_ref = None
                line.type_of_service_ref = None
                line.type_of_product_category_ref = None
            write_objects(write_con, lines, True, True)

def epip_scheduled_stop_point_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        ssp.stop_areas = None
        project_location_4326(ssp.location, generator_defaults)
        return ssp

    def query(read_database) -> Generator:
        with sqlite3.connect(read_database, check_same_thread=False) as read_con:
            _load_generator = load_generator(read_con, ScheduledStopPoint)
            for ssp in pool.imap_unordered(partial(process, generator_defaults=generator_defaults), _load_generator, chunksize=100):
                yield ssp

    with sqlite3.connect(write_database) as write_con:
        write_generator(write_con, ScheduledStopPoint, query(read_database), True)

# def epip_scheduled_stop_point2(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
#     print(sys._getframe().f_code.co_name)
#
#     with sqlite3.connect(read_database) as read_con:
#         with sqlite3.connect(write_database) as write_con:
#             scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
#             for ssp in scheduled_stop_points:
#                 ssp: ScheduledStopPoint
#                 ssp.stop_areas = None
#                 project_location_4326(ssp.location, generator_defaults)
#             print("processed")
#             write_objects(write_con, scheduled_stop_points, True, True)
#
# def epip_scheduled_stop_point3(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
#     print(sys._getframe().f_code.co_name)
#
#     def process(ssp: ScheduledStopPoint, generator_defaults: dict):
#         ssp.stop_areas = None
#         # project_location_4326(ssp.location, generator_defaults)
#         return ssp
#
#     def query(read_database) -> Generator:
#         with sqlite3.connect(read_database, check_same_thread=False) as read_con:
#             scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
#             for ssp in pool.imap_unordered(partial(process, generator_defaults=generator_defaults), scheduled_stop_points, chunksize=100):
#                 yield ssp
#
#     with sqlite3.connect(write_database) as write_con:
#         write_generator(write_con, ScheduledStopPoint, query(read_database), True)


def epip_scheduled_stop_point_memory(read_database: str, write_database: str, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
            for ssp in scheduled_stop_points:
                ssp: ScheduledStopPoint
                ssp.stop_areas = None
                project_location_4326(ssp.location, generator_defaults)

            write_objects(write_con, scheduled_stop_points, True, True)


def epip_timetabled_passing_times_memory(read_database, write_database, generator_defaults, dynamics=[]):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            # TODO: Maybe do this on the fly, per servicejourney?
            service_journey_patterns: List[ServiceJourneyPattern] = load_local(read_con, ServiceJourneyPattern)
            time_demand_types = load_local(read_con, TimeDemandType)
            service_journeys = load_local(read_con, ServiceJourney)

            timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

            # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
            timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)
            time_demand_types = None

            availability_conditions = load_local(read_con, AvailabilityCondition)
            servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
            service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
            write_objects(write_con, [service_calendar], True, False)

            for sj in service_journeys:
                sj: ServiceJourney
                sj.validity_conditions_or_valid_between = None
                sj.key_list = None
                sj.private_code = None

                # TODO: Benchmark
                any(map(lambda x: x(sj), dynamics))
                # for dynamic in dynamics:
                #     dynamic(sj)

            write_objects(write_con, service_journeys, True, False)

def apply_vehicle_type_to_sj(vt_by_sj: dict[ServiceJourneyRef, VehicleTypeRef], sj: ServiceJourney):
    sj.vehicle_type_ref_or_train_ref = vt_by_sj[getRef(sj)]

def apply_line_ref_to_sj(line_ref_by_sjp: dict[ServiceJourneyPatternRef, LineRef], sj: ServiceJourney):
    sj.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view = line_ref_by_sjp.get(sj.journey_pattern_ref)

def epip_timetabled_passing_times_generator2(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(sj: ServiceJourney, read_database, write_database, generator_defaults: dict):
        sj: ServiceJourney

        # Prototype, just: TimeDemandType -> PassingTimes
        with sqlite3.connect(read_database, check_same_thread=False) as read_con:
            service_journey_pattern: ServiceJourneyPattern = get_single(read_con, ServiceJourneyPattern, sj.journey_pattern_ref.ref, sj.journey_pattern_ref.version)
            time_demand_type: TimeDemandType = get_single(read_con, TimeDemandType, sj.time_demand_type_ref.ref, sj.time_demand_type_ref.version)
            CallsProfile.getPassingTimesFromTimeDemandType(sj, service_journey_pattern, time_demand_type)

        # TODO: AvailabilityCondition -> Uic

        sj.validity_conditions_or_valid_between = None
        sj.key_list = None
        sj.private_code = None
        return sj

    def query(read_database) -> Generator:
        with sqlite3.connect(read_database, check_same_thread=False) as read_con:
            _load_generator = load_generator(read_con, ServiceJourney)
            # for sj in _load_generator:
            #     yield process(sj, read_con, write_con, generator_defaults)
            for sj in pool.imap_unordered(partial(process, read_database=read_database, write_database=write_database, generator_defaults=generator_defaults), _load_generator, chunksize=100):
                yield sj

    with sqlite3.connect(write_database) as write_con:
        write_generator(write_con, ServiceJourney, query(read_database), True)


            # timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

            # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
            # timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)

            # availability_conditions = load_local(read_con, AvailabilityCondition)
            # servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])
            # service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
            # write_objects(write_con, [service_calendar], True, False)



def epip_service_journey_patterns(read_database, write_database, generator_defaults):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        with sqlite3.connect(write_database) as write_con:
            service_journey_patterns = load_local(read_con, ServiceJourneyPattern)
            infer_directions_from_sjps_and_apply(write_con, service_journey_patterns, generator_defaults)

            tmp_service_links = []
            for service_journey_pattern in service_journey_patterns:
                # The problem that may appear is that there are multiple routes, for single timing_links, dependend on the ServiceJourneyPattern
                # so in the case where this may happen, the academic correct way would change the id, and incorporate the route as well. This would
                # bring Route unique ServiceLinks, not a bad idea, but edge case.
                tmp_service_links += transform_timinglinks_to_servicelinks(read_con, service_journey_pattern)

            sls = {}
            for sl in tmp_service_links:
                sl: ServiceLink
                sl.operational_context_ref = None
                sl.line_string.id = sl.id.replace('ServiceLink', 'LineString').replace('-', '_').replace('#', '_').replace(':', '_')
                sls[sl.id] = sl

            service_links = list(sls.values())
            project_linestring(service_links, generator_defaults, 'EPSG:4326')
            write_objects(write_con, service_links, True, True)
            write_objects(write_con, service_journey_patterns, True, True)

def vehicle_type_from_block(read_database):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(read_database) as read_con:
        blocks: List[Block] = load_local(read_con, Block)
        sjs: dict[ServiceJourneyRef, VehicleTypeRef] = {}
        for block in blocks:
            vehicle_type: VehicleTypeRef = block.vehicle_type_ref_or_train_ref
            for journey in block.journeys.choice:
                if isinstance(journey, ServiceJourneyRef):
                    sjs[journey] = vehicle_type

        return sjs

def line_ref_from_route(read_database):
    with sqlite3.connect(read_database) as read_con:
        service_journey_patterns: List[ServiceJourneyPattern] = load_local(read_con, ServiceJourneyPattern)
        routes = getIndex(load_local(read_con, Route))
        line_ref_by_sjp: dict[ServiceJourneyPatternRef, LineRef] = {}
        for sjp in service_journey_patterns:
            line_ref_by_sjp[getRef(sjp)] = routes[sjp.route_ref_or_route_view.ref].line_ref

        return line_ref_by_sjp


generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1, 'DefaultLocationsystem': 'EPSG:28992'} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

def wrapper(func, kwargs):
    func(**kwargs)


#classes = get_interesting_classes()
#with sqlite3.connect("/tmp/target.sqlite") as con:
#    setup_database(con, classes, True)

# with Pool(10) as pool:
    # kwargs = {'read_database': "/home/netex/netex.sqlite", 'write_database': "/home/netex/target.sqlite", 'generator_defaults': generator_defaults}
#bison_codespaces("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)
    # epip_line_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
#epip_line_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

#epip_route_point_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

#epip_route_link_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)

#epip_scheduled_stop_point_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)
    # epip_scheduled_stop_point_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

    # epip_scheduled_stop_point("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
    # epip_scheduled_stop_point2("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
    # epip_scheduled_stop_point3("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

#epip_site_frame_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)
    # epip_route_point_memory(**kwargs)
    # epip_route_link_memory(**kwargs)


vt_by_sj = vehicle_type_from_block("/home/netex/netex.sqlite")
line_ref_by_sjp = line_ref_from_route("/home/netex/netex.sqlite")
epip_timetabled_passing_times_memory("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults,
                                     [
                                         partial(apply_vehicle_type_to_sj, vt_by_sj),
                                         partial(apply_line_ref_to_sj, line_ref_by_sjp)
                                      ])

epip_service_journey_patterns("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults)


    # epip_timetabled_passing_times_generator("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)
    # epip_timetabled_passing_times_generator2("/home/netex/netex.sqlite", "/home/netex/target.sqlite", generator_defaults, pool)

    # pool.starmap(wrapper, [(bison_codespaces, kwargs),
    #                        (epip_site_frame, kwargs),
    #                        (epip_route_point, kwargs),
    #                        (epip_route_link, kwargs),
    #                        (epip_scheduled_stop_point, kwargs),
    #                        (epip_timetabled_passing_times, kwargs),
    #                        (epip_service_journey_patterns, kwargs),
    #                        ])



# Voor alle PointsInJourneyPattern, als TimingLink een ServiceLink zou kunnen zijn, haal op basis van PointProjection de RouteLink op waar deze informatie
# in zou kunnen zitten. Doe dit niet exclusief op basis van From/To maar neem de Route die in het ServiceJourneyPattern staat mee als referentie.
# In het geval dat er sprake is van een TimingPointInJourneyPattern, haal dan de route op tot de eerst volgende ScheduledStopPoint en voeg de verschillende
# RouteLinks samen, houdt er rekening mee dat bij het samen voegen het laatste punt op de lijn gelijk is aan het eerste, en daarmee overgeslagen zou
# moeten worden.

# TODO: Mentz verzoek voor LineRef