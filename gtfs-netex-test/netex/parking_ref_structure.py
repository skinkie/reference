from dataclasses import dataclass
from .site_ref_structure import SiteRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingRefStructure(SiteRefStructure):
    value: RestrictedVar
