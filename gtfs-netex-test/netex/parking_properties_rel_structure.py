from dataclasses import dataclass, field
from typing import List
from netex.parking_properties import ParkingProperties
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingPropertiesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of PARKING PROPERTies.
    """
    class Meta:
        name = "parkingProperties_RelStructure"

    parking_properties: List[ParkingProperties] = field(
        default_factory=list,
        metadata={
            "name": "ParkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
