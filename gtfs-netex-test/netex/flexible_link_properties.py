from dataclasses import dataclass, field
from netex.flexible_link_properties_versioned_child_structure import FlexibleLinkPropertiesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleLinkProperties(FlexibleLinkPropertiesVersionedChildStructure):
    """
    Flexible properties of a LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
