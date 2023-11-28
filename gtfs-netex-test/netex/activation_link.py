from dataclasses import dataclass, field
from netex.activation_link_version_structure import ActivationLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationLink(ActivationLinkVersionStructure):
    """
    A LINK where a control process is activated when a vehicle passes it.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
