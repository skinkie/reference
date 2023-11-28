from dataclasses import dataclass
from netex.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicPlaceRef(TopographicPlaceRefStructure):
    """
    Reference to a TOPOGRAPHIC PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
