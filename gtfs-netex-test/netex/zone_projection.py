from dataclasses import dataclass, field
from netex.zone_projection_version_structure import ZoneProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneProjection(ZoneProjectionVersionStructure):
    """
    An oriented correspondence from one ZONE in a source layer,  onto a target
    entity : e.g.  POINT, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
