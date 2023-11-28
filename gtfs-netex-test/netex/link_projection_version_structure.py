from dataclasses import dataclass, field
from typing import Optional
from netex.link_ref_structure import LinkRefStructure
from netex.point_on_link_by_value_structure import PointOnLinkByValueStructure
from netex.point_on_link_ref_structure_1 import PointOnLinkRefStructure1
from netex.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a LINK PROJECTION.

    :ivar projected_link_ref: Link that is being projected. Can be
        omitted if given by context.
    :ivar project_to_link_ref: Link onto which projected LINK is being
        projected.
    :ivar start_point_on_link_ref_or_start_point_on_link_by_value:
    :ivar end_point_on_link_ref_or_end_point_on_link_by_value:
    """
    class Meta:
        name = "LinkProjection_VersionStructure"

    projected_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectedLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    project_to_link_ref: Optional[LinkRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_on_link_ref_or_start_point_on_link_by_value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartPointOnLinkRef",
                    "type": PointOnLinkRefStructure1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartPointOnLinkByValue",
                    "type": PointOnLinkByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    end_point_on_link_ref_or_end_point_on_link_by_value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndPointOnLinkRef",
                    "type": PointOnLinkRefStructure1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndPointOnLinkByValue",
                    "type": PointOnLinkByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
