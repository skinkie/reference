import duckdb as sqlite3
from typing import Iterable, Dict, Generator

from netexio.dbaccess import write_objects, load_generator, write_generator, update_generator
from netex import ServiceJourneyPattern, Direction, MultilingualString, DirectionType, ServiceJourney, DirectionRef
from refs import getId, getRef


def infer_directions_from_sjps_and_apply(read_database, write_database, generator_defaults: dict):
    directions: Dict[str, Direction] = {}
    direction_refs: Dict[str, DirectionRef] = {}

    def process(sjp: ServiceJourneyPattern, generator_defaults: dict):
        if sjp.direction_type is not None and sjp.direction_ref_or_direction_view is None:
            key = str(sjp.direction_type.value)
            direction: Direction = directions.get(key, None)
            if direction is None:
                direction = Direction(id=getId(Direction, generator_defaults['codespace'], key),
                                      version='any',
                                      name=MultilingualString(value=key),
                                      direction_type=DirectionType(value=sjp.direction_type))
                directions[key] = direction
                direction_refs[key] = getRef(direction)
            sjp.direction_ref_or_direction_view = direction_refs[key]
            return sjp

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, ServiceJourneyPattern)
        for sjp in _load_generator:
            new_sjp = process(sjp, generator_defaults)
            if new_sjp is not None:
                yield new_sjp

    # TODO: Make the database access pattern generic.
    with sqlite3.connect(write_database) as write_con:
        if write_database == read_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)
        update_generator(write_con, ServiceJourneyPattern, query(read_con))
        write_objects(write_con, list(directions.values()), True)