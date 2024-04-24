from dataclasses import dataclass

from .luggage_spot_version_structure import LuggageSpotVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpot(LuggageSpotVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
