from dataclasses import dataclass
from netex.topographic_place_derived_view_structure import TopographicPlaceDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicPlaceView(TopographicPlaceDerivedViewStructure):
    """Simplified view of TOPOGRAPHIC PLACE.

    Data is derived through the relationship.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
