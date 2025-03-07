from typing import Iterable, Dict, Generator

from netexio.database import Database
from netexio.dbaccess import write_objects, load_generator, write_generator, update_generator, load_local
from netex import ServiceJourneyPattern, Direction, MultilingualString, DirectionType, ServiceJourney, DirectionRef, \
    PassengerStopAssignment, StopPlace, LocationStructure2, Quay, ScheduledStopPoint, ScheduledStopPointRef, QuayRef, \
    StopPlaceRef
from refs import getId, getRef

def infer_locations_from_quay_or_stopplace_and_apply(db_read: Database, db_write: Database, generator_defaults: dict):
    mapping: Dict[str, LocationStructure2] = {}
    ssp_location: Dict[str, LocationStructure2] = {}

    def process(ssp: ScheduledStopPoint, generator_defaults: dict):
        if ssp.location is None:
            location: LocationStructure2 = ssp_location.get(ssp.id, None)
            if location is not None:
                ssp.location = location

        # TODO: The question here is can we just do something like a virtual table?
        return ssp

    def query(db_read: Database) -> Generator:
        _load_generator = load_generator(db_read, ScheduledStopPoint)
        for ssp in _load_generator:
            new_ssp = process(ssp, generator_defaults)
            if new_ssp is not None:
                yield new_ssp

    for sp in load_local(db_read, StopPlace):
        sp: StopPlace
        if sp.centroid is not None:
            mapping[sp.id] = sp.centroid.location
        if sp.quays is not None:
            for quay in sp.quays.taxi_stand_ref_or_quay_ref_or_quay:
                if isinstance(quay, Quay):
                    if quay.centroid is not None:
                        mapping[quay.id] = quay.centroid.location
                    elif sp.centroid is not None:
                        mapping[quay.id] = sp.centroid.location

    ssp_location = {}
    for psa in load_generator(db_read, PassengerStopAssignment):
        psa: PassengerStopAssignment
        if isinstance(psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point, ScheduledStopPointRef):
            if isinstance(psa.taxi_stand_ref_or_quay_ref_or_quay, QuayRef):
                if psa.taxi_stand_ref_or_quay_ref_or_quay.ref in mapping:
                    ssp_location[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = mapping[psa.taxi_stand_ref_or_quay_ref_or_quay.ref]
            if isinstance(psa.taxi_rank_ref_or_stop_place_ref_or_stop_place, StopPlaceRef):
                if psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref in mapping:
                   ssp_location[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = mapping[psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref]

    db_write.insert_objects_on_queue(ScheduledStopPoint, query(db_read))
