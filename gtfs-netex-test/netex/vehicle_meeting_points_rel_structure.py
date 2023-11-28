from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_point import VehicleMeetingPoint
from netex.vehicle_meeting_point_ref import VehicleMeetingPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE MEETING POINTs.
    """
    class Meta:
        name = "vehicleMeetingPoints_RelStructure"

    vehicle_meeting_point_ref_or_vehicle_meeting_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleMeetingPointRef",
                    "type": VehicleMeetingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPoint",
                    "type": VehicleMeetingPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
