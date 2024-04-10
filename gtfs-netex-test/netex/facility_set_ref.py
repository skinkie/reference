from dataclasses import dataclass

from .facility_set_ref_structure import FacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySetRef(FacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
