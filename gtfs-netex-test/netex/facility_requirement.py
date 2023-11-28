from dataclasses import dataclass, field
from netex.facility_requirement_version_structure import FacilityRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FacilityRequirement(FacilityRequirementVersionStructure):
    """
    Requirements for carrying passengers.

    :ivar id: Identifier of FACILITY REQUIREMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
