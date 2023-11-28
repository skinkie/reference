from dataclasses import dataclass, field
from netex.topographic_projection_version_structure import TopographicProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicProjection(TopographicProjectionVersionStructure):
    """An correspondence from a ZONE in a source layer,  onto a name place: i.e.
    TOPOGRAPHIC PLACE.

    +v1.1

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
