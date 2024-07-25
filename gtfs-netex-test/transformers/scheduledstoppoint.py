import duckdb as sqlite3
from typing import Iterable, Dict, Generator

from netexio.dbaccess import write_objects, load_generator, write_generator, update_generator, load_local
from netex import ServiceJourneyPattern, Direction, MultilingualString, DirectionType, ServiceJourney, DirectionRef, \
    PassengerStopAssignment, StopPlace, LocationStructure2, Quay, ScheduledStopPoint, ScheduledStopPointRef, QuayRef, \
    StopPlaceRef
from refs import getId, getRef

def infer_locations_from_quay_or_stopplace_and_apply(read_database, write_database, generator_defaults: dict):
    mapping: Dict[str, LocationStructure2] = {}
    ssp_location: Dict[str, LocationStructure2] = {}

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        if ssp.location is None:
            location: LocationStructure2 = ssp_location.get(ssp.id, None)
            if location is not None:
                ssp.location = location
                return ssp

    def query(read_con) -> Generator:
        _load_generator = load_generator(read_con, ScheduledStopPoint)
        for ssp in _load_generator:
            new_ssp = process(ssp, generator_defaults)
            if new_ssp is not None:
                yield new_ssp

    # TODO: Make the database access pattern generic.
    with sqlite3.connect(write_database) as write_con:
        if write_database == read_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database, read_only=True)

        for sp in load_local(read_con, StopPlace):
            sp: StopPlace
            mapping[sp.id] = sp.centroid.location
            if sp.quays is not None:
                for quay in sp.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    if isinstance(quay, Quay):
                        mapping[quay.id] = quay.centroid.location

        ssp_location = {}
        for psa in load_generator(read_con, PassengerStopAssignment):
            psa: PassengerStopAssignment
            if isinstance(psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point, ScheduledStopPointRef):
                if isinstance(psa.taxi_stand_ref_or_quay_ref_or_quay, QuayRef):
                    ssp_location[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = mapping[psa.taxi_stand_ref_or_quay_ref_or_quay.ref]
                if isinstance(psa.taxi_rank_ref_or_stop_place_ref_or_stop_place, StopPlaceRef):
                    ssp_location[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = mapping[psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref]

        update_generator(write_con, ScheduledStopPoint, query(read_con))
