from dataclasses import dataclass, field
from netex.point_on_line_section_versioned_child_structure import PointOnLineSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOnLineSection(PointOnLineSectionVersionedChildStructure):
    """Inclusion of a POINT on a LINE SECTION.

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
