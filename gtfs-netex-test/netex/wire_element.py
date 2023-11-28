from dataclasses import dataclass, field
from netex.wire_element_version_structure import WireElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class WireElement(WireElementVersionStructure):
    """
    A type of INFRASTRUCTURE LINK used to describe a WIRE network.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
