from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    CAR_PARK = "carPark"
    PARK_AND_RIDE_PARK = "parkAndRidePark"
    MOTORCYCLE_PARK = "motorcyclePark"
    CYCLE_PARK = "cyclePark"
    RENTAL_CAR_PARK = "rentalCarPark"
    COACH_PARK = "coachPark"
