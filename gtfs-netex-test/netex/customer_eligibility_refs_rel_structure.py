from dataclasses import dataclass, field
from typing import List
from netex.commercial_profile_eligibility_ref import CommercialProfileEligibilityRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.residential_qualification_eligibility_ref import ResidentialQualificationEligibilityRef
from netex.user_profile_eligibility_ref import UserProfileEligibilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerEligibilityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of USER PROFILE ELIGIBILITies.
    """
    class Meta:
        name = "customerEligibilityRefs_RelStructure"

    residential_qualification_eligibility_ref_or_commercial_profile_eligibility_ref_or_user_profile_eligibility_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResidentialQualificationEligibilityRef",
                    "type": ResidentialQualificationEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileEligibilityRef",
                    "type": CommercialProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileEligibilityRef",
                    "type": UserProfileEligibilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
