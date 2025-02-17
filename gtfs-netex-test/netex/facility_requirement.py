from dataclasses import dataclass

from .facility_requirement_version_structure import FacilityRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FacilityRequirement(FacilityRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
