from dataclasses import dataclass, field
from netex.flexible_quay_version_structure import FlexibleQuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleQuay(FlexibleQuayVersionStructure):
    """
    A ZONE of physical access to public transport vehicles such as a platform.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
