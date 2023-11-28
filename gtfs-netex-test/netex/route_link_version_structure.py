from dataclasses import dataclass, field
from typing import Optional
from netex.link_version_structure import LinkVersionStructure
from netex.mode_restriction_assessments_rel_structure import ModeRestrictionAssessmentsRelStructure
from netex.operational_context_ref import OperationalContextRef
from netex.route_point_ref_structure import RoutePointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RouteLinkVersionStructure(LinkVersionStructure):
    """
    Type for ROUTE LINK.

    :ivar from_point_ref: Identifier of ROUTE POINT from which Link
        starts.
    :ivar to_point_ref: Identifier of ROUTE POINT at which Link ends.
    :ivar operational_context_ref:
    :ivar mode_restriction_assessments: Mode restriction assessments for
        ROUTE LINK +v1.2.2
    """
    class Meta:
        name = "RouteLink_VersionStructure"

    from_point_ref: RoutePointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: RoutePointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mode_restriction_assessments: Optional[ModeRestrictionAssessmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "modeRestrictionAssessments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
