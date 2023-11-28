from dataclasses import dataclass, field
from netex.controllable_element_version_structure import ControllableElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControllableElement(ControllableElementVersionStructure):
    """
    The smallest controllable element of public transport consumption, all along
    which any VALIDITY PARAMETER ASSIGNMENT remains valid.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
