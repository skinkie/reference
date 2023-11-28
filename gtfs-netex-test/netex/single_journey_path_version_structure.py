from dataclasses import dataclass, field
from typing import Optional
from netex.route_ref import RouteRef
from netex.section_in_sequence_versioned_child_structure import LinkSequenceVersionStructure
from netex.vehicle_meeting_points_in_sequence_rel_structure import VehicleMeetingPointsInSequenceRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleJourneyPathVersionStructure(LinkSequenceVersionStructure):
    """Type for SINGLE JOURNEY PATH.

    +v1.2.2
    """
    class Meta:
        name = "SingleJourneyPath_VersionStructure"

    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_sequence: Optional[VehicleMeetingPointsInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
