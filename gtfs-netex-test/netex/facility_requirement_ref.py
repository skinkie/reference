from dataclasses import dataclass
from netex.facility_requirement_ref_structure import FacilityRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FacilityRequirementRef(FacilityRequirementRefStructure):
    """
    Reference to a FACILITY REQUIREMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
