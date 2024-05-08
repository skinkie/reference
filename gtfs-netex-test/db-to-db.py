import sqlite3
from typing import List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler, lxml
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import ServiceJourneyPattern, Direction, Codespace, MultilingualString, DirectionType, ServiceJourney, \
    AvailabilityCondition, TimeDemandType
from refs import getId, getRef
from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.indent = None
serializer_config.xml_declaration = False
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

def write_objects(con, objs, empty=False, many=False):
    cur = con.cursor()
    clazz = objs[0].__class__
    objectname = getattr(clazz.Meta, 'name', clazz.__name__)
   

    if empty:
        sql_drop_table = f"DROP TABLE IF EXISTS {objectname}"
        cur.execute(sql_drop_table)

    sql_create_table = f"CREATE TABLE IF NOT EXISTS {objectname} (id varchar(64) NOT NULL, version varchar(64) NOT NULL, object text NOT NULL, PRIMARY KEY (id, version));"
    cur.execute(sql_create_table)

    if many:
        print(objectname, len(objs))
        cur.executemany(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', [(obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')) for obj in objs])
    else:
        for i in range(0, len(objs)):
            obj = objs[i]
            cur.execute(f'INSERT INTO {objectname} (id, version, object) VALUES (?, ?, ?);', (obj.id, obj.version, serializer.render(obj, ns_map).replace('\n', '').encode('utf-8')))
            print('\r', str(i), end = '')
        print('\r', end='')

def infer_directions_from_sjps_and_apply(con, service_journey_patterns: List[ServiceJourneyPattern], generator_defaults):
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

def load_local(con, clazz, limit=None):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    if limit is not None:
        cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    else:
        cur.execute(f"SELECT object FROM {type};")


    objs = []
    for xml, in cur.fetchall():
        obj = parser.from_bytes(xml, clazz)
        objs.append(obj)

    return objs

def load_generator(con, clazz):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    cur.execute(f"SELECT object FROM {type};")

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield parser.from_bytes(xml[0], clazz)

generator_defaults = {'codespace': Codespace(xmlns='OPENOV'), 'version': 1} # Invent something, that materialises the refs, so VersionFrameDefaultsStructure can be used

with sqlite3.connect("/tmp/netex.sqlite") as con:
    service_journey_patterns = load_local(con, ServiceJourneyPattern)
    time_demand_types = load_local(con, TimeDemandType)
    service_journeys = load_local(con, ServiceJourney, 10)

    timetabledpassingtimesprofile = TimetablePassingTimesProfile(generator_defaults['codespace'], generator_defaults['version'], service_journeys, service_journey_patterns, time_demand_types)

    # TODO: Implement getTimetabledPassingTimes incrementally. As generator won't work, since it has to store the result (directly).
    timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)
    time_demand_types = None

    availability_conditions = load_local(con, AvailabilityCondition)
    servicecalendarepip = ServiceCalendarEPIPFrame(generator_defaults['codespace'])

    with sqlite3.connect("/tmp/target.sqlite") as con2:
        service_calendar = servicecalendarepip.availabilityConditionsToServiceCalendar(service_journeys, availability_conditions)
        availability_conditions = None
        write_objects(con2, [service_calendar], True, False)
        service_calendar = None
        infer_directions_from_sjps_and_apply(con2, service_journey_patterns, generator_defaults)
        write_objects(con2, service_journey_patterns, True, True)
        service_journey_patterns = None
        for sj in service_journeys:
            sj: ServiceJourney
            sj.validity_conditions_or_valid_between = None
            sj.key_list = None
            sj.private_code = None

        write_objects(con2, service_journeys, True, False)
        service_journeys = None

