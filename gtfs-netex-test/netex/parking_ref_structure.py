from dataclasses import dataclass

from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingRefStructure(SiteRefStructure):
    pass
