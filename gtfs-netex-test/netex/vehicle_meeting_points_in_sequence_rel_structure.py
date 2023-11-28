from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_point_in_path import VehicleMeetingPointInPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointsInSequenceRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of a VEHICLE MEETING POINTS in Sequence.

    :ivar vehicle_meeting_point_in_path: A group of VEHICLE JOURNEYs
        following the same JOURNEY PATTERN having the same HEADWAY
        INTERVAL between a specified start and end time (for example,
        every 10 min). This is especially useful for passenger
        information.
    """
    class Meta:
        name = "vehicleMeetingPointsInSequence_RelStructure"

    vehicle_meeting_point_in_path: List[VehicleMeetingPointInPath] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointInPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
