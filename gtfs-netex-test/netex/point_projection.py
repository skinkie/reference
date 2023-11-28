from dataclasses import dataclass, field
from netex.point_projection_version_structure import PointProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointProjection(PointProjectionVersionStructure):
    """
    An oriented correspondence from one POINT of a source layer, onto a entity in a
    target layer:  e.g. POINT, LINK, LINK SEQUENCE, COMPLEX FEATURE, within a
    defined TYPE OF PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
