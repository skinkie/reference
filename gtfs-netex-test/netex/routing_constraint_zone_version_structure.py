from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.group_of_lines_ref import GroupOfLinesRef
from netex.line_refs_rel_structure import LineRefsRelStructure
from netex.network_ref import NetworkRef
from netex.points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from netex.zone_use_enumeration import ZoneUseEnumeration
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoutingConstraintZoneVersionStructure(ZoneVersionStructure):
    """
    Type for ROUTING CONSTRAINT ZONE.

    :ivar zone_use: How ZONE may be used.
    :ivar maximum_speed: Maximum speed in ZONE. +v1.2.2ne
    :ivar points_in_pattern: Points that constraint limits to, in
        sequence.
    :ivar lines: LINEs associated with ROUTING CONSTRAINT ZONE.
    :ivar network_ref_or_group_of_lines_ref:
    """
    class Meta:
        name = "RoutingConstraintZone_VersionStructure"

    zone_use: Optional[ZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumSpeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_in_pattern: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_ref_or_group_of_lines_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
