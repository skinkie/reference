from dataclasses import dataclass, field
from netex.flexible_point_properties_versioned_child_structure import FlexiblePointPropertiesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexiblePointProperties(FlexiblePointPropertiesVersionedChildStructure):
    """
    Flexible properties of a POINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
