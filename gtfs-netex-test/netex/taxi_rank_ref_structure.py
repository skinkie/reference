from dataclasses import dataclass
from netex.stop_place_ref_structure import StopPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiRankRefStructure(StopPlaceRefStructure):
    """
    Type for a reference to a TAXI RANK.
    """
