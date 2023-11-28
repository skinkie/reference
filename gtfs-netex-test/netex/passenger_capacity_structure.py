from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCapacityStructure(DataManagedObjectStructure):
    """
    Capacity for a VEHICLE TYPE and Class.

    :ivar fare_class: Edit care class for which capacity is specifyed.
        Default is any, i.e. capacity is for all classes.
    :ivar total_capacity: The total capacity of vehicles of the type.
        For a requirement this is the minimum needed.
    :ivar seating_capacity: The seating capacity of vehicles of the
        type. For a requirement this is the minimum needed.
    :ivar standing_capacity: The standing capacity of vehicles of the
        type.  For a requirement this is the minimum needed.
    :ivar special_place_capacity: The number of special places on
        vehicles of the type, e.g. seats for the disabled. For a
        requirement this is the minimum needed.
    :ivar pushchair_capacity: The number of push chair places on
        vehicles of the type. For a requirement this is the minimum
        needed.
    :ivar wheelchair_place_capacity: The number of wheelchairs places on
        vehicles of the type. For a requirement this is the minimum
        needed.
    """
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    seating_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standing_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pushchair_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
