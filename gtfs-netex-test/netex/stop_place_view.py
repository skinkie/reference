from dataclasses import dataclass
from netex.stop_place_derived_view_structure import StopPlaceDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceView(StopPlaceDerivedViewStructure):
    """Simplified view of STOP PLACE.

    Contains.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
