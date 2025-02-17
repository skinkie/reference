from dataclasses import dataclass

from .topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TopographicPlaceRef(TopographicPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
