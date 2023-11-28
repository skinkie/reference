from dataclasses import dataclass
from netex.luggage_service_ref_structure import LuggageServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LuggageServiceRef(LuggageServiceRefStructure):
    """
    Identifier of an LUGGAGE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
