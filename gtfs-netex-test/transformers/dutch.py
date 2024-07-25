import sys
from functools import partial
from typing import Generator, Dict

import duckdb as sqlite3

from netexio.dbaccess import load_generator, write_generator, load_local, write_objects
from netex import ScheduledStopPoint, Codespace, Version, ServiceJourney
from multiprocessing import Pool

from refs import getIndex
from timedemandtypesprofile import TimeDemandTypesProfile
from transformers.projection import project_location

import time


def dutch_scheduled_stop_point_generator(read_database: str, write_database: str, generator_defaults: dict, pool: Pool):
    print(sys._getframe().f_code.co_name)

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        project_location(ssp.location, "EPSG:28992", generator_defaults, quantize='1.0')
        return ssp

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, ScheduledStopPoint)
        for ssp in pool.imap_unordered(partial(process, generator_defaults=generator_defaults), _load_generator, chunksize=100):
            yield ssp

    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database, read_only=True)

        write_generator(write_con, ScheduledStopPoint, query(read_con), True)

def dutch_scheduled_stop_point_memory(read_database: str, write_database: str, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database, read_only=True)

        scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
        for ssp in scheduled_stop_points:
            ssp: ScheduledStopPoint
            ssp.stop_areas = None
            if ssp.location is not None:
                project_location(ssp.location, "EPSG:28992", generator_defaults, quantize='1.0')
            else:
                print(f"ScheduledStopPoint {ssp.id} does not have a location.")

        write_objects(write_con, scheduled_stop_points, True, True)

def dutch_service_journey_pattern_time_demand_type_memory(read_database: str, write_database: str, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        if read_database == write_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database, read_only=True)

        codespaces = load_local(read_con, Codespace, 1)
        versions = load_local(read_con, Version, 1)
        ssps: Dict[str, ScheduledStopPoint] = getIndex(load_local(read_con, ScheduledStopPoint))

        tdtp = TimeDemandTypesProfile(codespace=codespaces[0], version=versions[0])

        i = 0

        now = time.time()
        print("_load_generator: ", now, int(0))
        _load_generator = load_generator(read_con, ServiceJourney)

        _prev = now
        now = time.time()
        print("for loop: ", now, int(now - _prev))
        for sj in _load_generator:
            sjp = tdtp.getServiceJourneyPatternGenerator(read_con, write_con, sj, ssps)
            tdtp.getTimeDemandTypeGenerator(read_con, write_con, sj, ssps)
            sj.calls = None
            write_objects(write_con, [sj], False, False, silent=True)
            i += 1
            if i % 100 == 0:
                _prev = now
                now = time.time()
                print("\r", "ServiceJourney", str(i), str(now), str(int(now - _prev)))
        print("\n")
        _prev = now
        now = time.time()
        print("done: ", now, int(now - _prev))
