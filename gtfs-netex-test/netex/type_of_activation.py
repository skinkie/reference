from dataclasses import dataclass, field
from netex.type_of_activation_value_structure import TypeOfActivationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfActivation(TypeOfActivationValueStructure):
    """
    A classification of real-time processes that are activated when vehicles passes
    an ACTIVATION POINT or an ACTIVATION LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
