from dataclasses import dataclass, field
from netex.activation_point_version_structure import ActivationPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationPoint(ActivationPointVersionStructure):
    """A POINT where a control process is activated when a vehicle passes it.

    EQUIPMENT may be needed for the activation.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
