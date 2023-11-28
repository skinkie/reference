from dataclasses import dataclass
from netex.stop_place_entrance_ref_structure import StopPlaceEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceEntranceRef(StopPlaceEntranceRefStructure):
    """
    Reference to a STOP PLACE ENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
