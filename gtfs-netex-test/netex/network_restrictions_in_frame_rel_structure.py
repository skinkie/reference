from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.meeting_restriction import MeetingRestriction
from netex.overtaking_possibility import OvertakingPossibility
from netex.restricted_manoeuvre import RestrictedManoeuvre
from netex.vehicle_type_at_point import VehicleTypeAtPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of NETWORK RESTRICTION.
    """
    class Meta:
        name = "networkRestrictionsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OvertakingPossibility",
                    "type": OvertakingPossibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingRestriction",
                    "type": MeetingRestriction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedManoeuvre",
                    "type": RestrictedManoeuvre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeAtPoint",
                    "type": VehicleTypeAtPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
