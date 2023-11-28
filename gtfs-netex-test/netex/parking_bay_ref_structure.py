from dataclasses import dataclass
from netex.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayRefStructure(SiteComponentRefStructure):
    """
    Type for a reference to a PARKING BAY.
    """
