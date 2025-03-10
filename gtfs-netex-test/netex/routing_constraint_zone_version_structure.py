from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .group_of_lines_ref import GroupOfLinesRef
from .line_refs_rel_structure import LineRefsRelStructure
from .lines_in_direction_refs_rel_structure import LinesInDirectionRefsRelStructure
from .network_ref import NetworkRef
from .points_in_journey_pattern_rel_structure import PointsInJourneyPatternRelStructure
from .zone_use_enumeration import ZoneUseEnumeration
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoutingConstraintZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "RoutingConstraintZone_VersionStructure"

    zone_use: Optional[ZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumSpeed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_pattern: Optional[PointsInJourneyPatternRelStructure] = field(
        default=None,
        metadata={
            "name": "pointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_directions: Optional[LinesInDirectionRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "lineDirections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_lines_ref: Optional[Union[NetworkRef, GroupOfLinesRef]] = field(
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
        },
    )
