from dataclasses import dataclass
from netex.left_luggage_service_ref_structure import LeftLuggageServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LeftLuggageServiceRef(LeftLuggageServiceRefStructure):
    """
    Identifier of an LEFT LUGGAGE SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
