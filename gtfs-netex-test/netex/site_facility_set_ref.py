from dataclasses import dataclass
from .site_facility_set_ref_structure import SiteFacilitySetRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySetRef(SiteFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
