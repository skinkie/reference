from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerCapacityStructure(DataManagedObjectStructure):
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    seating_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standing_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    special_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pushchair_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pram_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bicycle_rack_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleRackCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
