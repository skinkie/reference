from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_link import VehicleMeetingLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingLinksInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE MEETING LINKs.
    """
    class Meta:
        name = "vehicleMeetingLinksInFrame_RelStructure"

    vehicle_meeting_link: List[VehicleMeetingLink] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
