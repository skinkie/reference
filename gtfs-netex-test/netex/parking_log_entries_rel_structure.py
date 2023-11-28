from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking_bay_condition import ParkingBayCondition
from netex.parking_bay_condition_ref import ParkingBayConditionRef
from netex.rental_availability import RentalAvailability
from netex.rental_availability_ref import RentalAvailabilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingLogEntriesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING LOG ENTRYs.
    """
    class Meta:
        name = "parkingLogEntries_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingBayConditionRef",
                    "type": ParkingBayConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RentalAvailabilityRef",
                    "type": RentalAvailabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
