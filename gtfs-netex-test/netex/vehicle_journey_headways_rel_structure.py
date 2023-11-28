from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.vehicle_journey_headway import VehicleJourneyHeadway

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyHeadwaysRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of a VEHICLE JOURNEY FREQUENCies.

    :ivar vehicle_journey_headway: VEHICLE JOURNEY FREQUENCY for a
        specified TIME DEMAND TYPE.
    """
    class Meta:
        name = "vehicleJourneyHeadways_RelStructure"

    vehicle_journey_headway: List[VehicleJourneyHeadway] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
