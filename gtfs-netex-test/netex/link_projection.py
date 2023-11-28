from dataclasses import dataclass, field
from netex.link_projection_version_structure import LinkProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkProjection(LinkProjectionVersionStructure):
    """
    An oriented correspondence from one LINK of a source layer, onto an entity in a
    target layer: e.g. LINK SEQUENCE, COMPLEX FEATURE, within a defined TYPE OF
    PROJECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
