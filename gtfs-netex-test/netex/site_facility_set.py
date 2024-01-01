from dataclasses import dataclass
from .site_facility_set_structure import SiteFacilitySetStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySet(SiteFacilitySetStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
