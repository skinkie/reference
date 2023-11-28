from dataclasses import dataclass
from netex.stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceRef(StopPlaceRefStructure):
    """
    Reference to a STOP PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
