from dataclasses import dataclass

from .facility_set_version_structure import FacilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySet(FacilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
