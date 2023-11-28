from dataclasses import dataclass
from netex.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingRefStructure(SiteRefStructure):
    """
    Type for a reference to a PARKING.
    """
