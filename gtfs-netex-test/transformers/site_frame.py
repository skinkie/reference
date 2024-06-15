import sys
import duckdb as sqlite3
from itertools import groupby
from typing import List, Generator, Tuple

from dbaccess import load_local, write_objects, write_generator
from refs import getIndex, getRef
from utils import project

import duckdb as sqlite

from netex import ScheduledStopPoint, StopArea, StopPlace, Quay, QuaysRelStructure, SimplePointVersionStructure, \
    PassengerStopAssignment


def infer_stop_place_from_scheduled_stop_point(scheduled_stop_point: ScheduledStopPoint) -> (StopPlace, List[PassengerStopAssignment]):
    quay: Quay = project(scheduled_stop_point, Quay)
    quay.centroid = SimplePointVersionStructure(location=scheduled_stop_point.location)
    stop_place: StopPlace = project(scheduled_stop_point, StopPlace)
    stop_place.centroid = SimplePointVersionStructure(location=scheduled_stop_point.location)
    stop_place.quays = QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[quay])
    passenger_stop_assignment: PassengerStopAssignment = project(scheduled_stop_point, PassengerStopAssignment)
    passenger_stop_assignment.order = 1
    passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point = getRef(scheduled_stop_point)
    passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay = getRef(quay)
    return stop_place, [passenger_stop_assignment]

def infer_stop_place_from_stop_area(stop_area: StopArea, scheduled_stop_points: List[ScheduledStopPoint]) -> (StopPlace, List[PassengerStopAssignment]):
    def ssp_to_quay(scheduled_stop_point: ScheduledStopPoint):
        quay: Quay = project(scheduled_stop_point, Quay)
        quay.centroid = SimplePointVersionStructure(location=scheduled_stop_point.location)
        passenger_stop_assignment: PassengerStopAssignment = project(scheduled_stop_point, PassengerStopAssignment)
        passenger_stop_assignment.order = 1
        passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point = getRef(scheduled_stop_point)
        passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay = getRef(quay)
        return quay, passenger_stop_assignment

    stop_place: StopPlace = project(stop_area, StopPlace)
    quay_psa = [ssp_to_quay(ssp) for ssp in scheduled_stop_points]
    stop_place.quays = QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[quay_psa[0] for quay_psa in quay_psa])
    return stop_place, [quay_psa[1] for quay_psa in quay_psa]

def groupby_stop_area(stop_areas: List[StopArea], scheduled_stop_points: List[ScheduledStopPoint]) -> Generator[Tuple[StopPlace, List[PassengerStopAssignment]], None, None]:
    stop_areas = getIndex(stop_areas)
    ssp_to_stop_area_ref = groupby([ssp for ssp in scheduled_stop_points if ssp.stop_areas is not None and len(ssp.stop_areas.stop_area_ref) > 0], lambda x: x.stop_areas.stop_area_ref[0])
    for stop_area_ref, ssps in ssp_to_stop_area_ref:
        yield infer_stop_place_from_stop_area(stop_areas[stop_area_ref], ssps)
    for ssp in [ssp for ssp in scheduled_stop_points if ssp.stop_areas is None or len(ssp.stop_areas.stop_area_ref) == 0]:
        yield infer_stop_place_from_scheduled_stop_point(ssp)

def infer_stop_places(read_database: str, write_database: str, generator_defaults: dict):
    print(sys._getframe().f_code.co_name)
    with sqlite3.connect(write_database) as write_con:
        if write_database == read_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database)

        stop_areas = load_local(read_con, StopArea)
        scheduled_stop_points = load_local(read_con, ScheduledStopPoint)
        write_generator(write_con, StopPlace, [], True)
        write_generator(write_con, PassengerStopAssignment, [], True)

        # TODO: How to write to the database, a pair of input from a generator?
        for stop_place, psas in groupby_stop_area(stop_areas, scheduled_stop_points):
            write_objects(write_con, [stop_place], False, False)
            write_objects(write_con, psas, False, False)
