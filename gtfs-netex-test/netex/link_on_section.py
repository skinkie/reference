from dataclasses import dataclass, field
from netex.link_on_section_versioned_child_structure import LinkOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkOnSection(LinkOnSectionVersionedChildStructure):
    """LINK on a SECTION.

    +v1.1.

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
