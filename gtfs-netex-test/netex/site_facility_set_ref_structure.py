from dataclasses import dataclass

from .facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteFacilitySetRefStructure(FacilitySetRefStructure):
    pass
