from dataclasses import dataclass, field
from netex.point_on_section_versioned_child_structure import PointOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnSection(PointOnSectionVersionedChildStructure):
    """POINT  on a SECTION.

    +v1.1.

    :ivar id: Identifier of POINT ON SECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
