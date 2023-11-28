from dataclasses import dataclass
from netex.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleStopPlaceRefStructure(PlaceRefStructure):
    """
    Type for a reference to a FLEXIBLE STOP PLACE.
    """
