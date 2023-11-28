from dataclasses import dataclass, field
from netex.flexible_line_version_structure import FlexibleLineVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleLine(FlexibleLineVersionStructure):
    """
    A group of FLEXIBLE ROUTEs of which is generally known to the public by a
    similar name or number and which have common booking arrangements.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
