from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_point import VehicleMeetingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointsInFrameRelStructure(ContainmentAggregationStructure):
    """Type for a list of references to a VEHICLE MEETING POINTs.

    in Frame
    """
    class Meta:
        name = "vehicleMeetingPointsInFrame_RelStructure"

    vehicle_meeting_point: List[VehicleMeetingPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
