from dataclasses import dataclass
from netex.stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QuayRefStructure(StopPlaceSpaceRefStructure):
    """
    Type for reference to a QUAY.
    """
