from dataclasses import dataclass
from netex.luggage_allowance_ref_structure import LuggageAllowanceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageAllowanceRef(LuggageAllowanceRefStructure):
    """
    Reference to a LUGGAGE ALLOWANCE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
