from dataclasses import dataclass

from .luggage_spot_ref_structure import LuggageSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpotRef(LuggageSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
