from dataclasses import dataclass, field
from typing import Optional
from netex.point_ref_structure import PointRefStructure
from netex.point_refs_rel_structure import PointRefsRelStructure
from netex.projection_version_structure import ProjectionVersionStructure
from netex.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneProjectionVersionStructure(ProjectionVersionStructure):
    """
    Type for a ZONE PROJECTION.

    :ivar projected_zone_ref: ZONE being projected.
    :ivar project_to_zone_ref: Reference to ZONE onto to which ZONE
        projects.
    :ivar project_to_point_ref: Reference to POINT to which centre of
        ZONE projects.
    :ivar points: Sequence of points making up PROJECTION.
    """
    class Meta:
        name = "ZoneProjection_VersionStructure"

    projected_zone_ref: ZoneRefStructure = field(
        metadata={
            "name": "ProjectedZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    project_to_zone_ref: Optional[ZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    project_to_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ProjectToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    points: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
