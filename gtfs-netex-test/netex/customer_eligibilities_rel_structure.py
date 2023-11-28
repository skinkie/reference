from dataclasses import dataclass, field
from typing import List
from netex.commercial_profile_eligibility import CommercialProfileEligibility
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.residential_qualification_eligibility import ResidentialQualificationEligibility
from netex.user_profile_eligibility import UserProfileEligibility

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerEligibilitiesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of CUSTOMER ELIGIBILITY.s.
    """
    class Meta:
        name = "customerEligibilities_RelStructure"

    residential_qualification_eligibility_or_commercial_profile_eligibility_or_user_profile_eligibility: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibility",
                    "type": ResidentialQualificationEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibility",
                    "type": CommercialProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibility",
                    "type": UserProfileEligibility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
