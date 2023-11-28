from dataclasses import dataclass, field
from netex.luggage_allowance_version_structure import LuggageAllowanceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageAllowance(LuggageAllowanceVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
