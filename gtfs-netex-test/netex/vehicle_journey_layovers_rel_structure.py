from dataclasses import dataclass, field
from typing import List
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.vehicle_journey_layover import VehicleJourneyLayover

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyLayoversRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of for a VEHICLE JOURNEY LAYOVERs.

    :ivar vehicle_journey_layover: VEHICLE JOURNEY LAYOVER for a
        specified TIME DEMAND TYPE.
    """
    class Meta:
        name = "vehicleJourneyLayovers_RelStructure"

    vehicle_journey_layover: List[VehicleJourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
