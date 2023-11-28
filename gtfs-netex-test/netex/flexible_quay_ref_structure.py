from dataclasses import dataclass
from netex.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleQuayRefStructure(PlaceRefStructure):
    """
    Type for reference to a FLEXIBLE QUAY.
    """
