from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.facility_requirement import FacilityRequirement
from netex.facility_requirement_ref import FacilityRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FacilityRequirementsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FACILITY REQUIREMENTs.
    """
    class Meta:
        name = "facilityRequirements_RelStructure"

    facility_requirement_ref_or_facility_requirement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FacilityRequirementRef",
                    "type": FacilityRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirement",
                    "type": FacilityRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
