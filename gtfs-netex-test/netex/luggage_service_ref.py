from dataclasses import dataclass

from .luggage_service_ref_structure import LuggageServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LuggageServiceRef(LuggageServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
