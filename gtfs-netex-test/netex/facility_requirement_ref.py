from dataclasses import dataclass
from .facility_requirement_ref_structure import FacilityRequirementRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementRef(FacilityRequirementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
