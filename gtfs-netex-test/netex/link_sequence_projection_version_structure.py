from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.line_string import LineString
from netex.link_sequence_ref_structure import LinkSequenceRefStructure
from netex.point_refs_rel_structure import PointRefsRelStructure
from netex.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkSequenceProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a LINK SEQUENCE PROJECTION.

    :ivar projected_link_sequence_ref: LINK SEQUENCE that is being
        projected. Can be omitted if given by context.
    :ivar distance: Distance Travelled.
    :ivar points_or_line_string:
    """
    class Meta:
        name = "LinkSequenceProjection_VersionStructure"

    projected_link_sequence_ref: Optional[LinkSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedLinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points_or_line_string: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "points",
                    "type": PointRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        }
    )
