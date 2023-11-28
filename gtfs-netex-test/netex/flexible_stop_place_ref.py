from dataclasses import dataclass
from netex.flexible_stop_place_ref_structure import FlexibleStopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleStopPlaceRef(FlexibleStopPlaceRefStructure):
    """
    Reference to a FLEXIBLE STOP PLACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
