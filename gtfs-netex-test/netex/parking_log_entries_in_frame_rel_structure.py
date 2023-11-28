from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking_bay_condition import ParkingBayCondition
from netex.rental_availability import RentalAvailability

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingLogEntriesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING LOG ENTRYs in a frame.
    """
    class Meta:
        name = "parkingLogEntriesInFrame_RelStructure"

    parking_bay_condition_or_rental_availability: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingBayCondition",
                    "type": ParkingBayCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailability",
                    "type": RentalAvailability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
