from dataclasses import dataclass, field
from typing import Optional
from netex.commercial_profile_ref import CommercialProfileRef
from netex.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    """
    Type for COMMERCIAL PROFILE ELIGIBILITY.
    """
    class Meta:
        name = "CommercialProfileEligibility_VersionedChildStructure"

    commercial_profile_ref: Optional[CommercialProfileRef] = field(
        default=None,
        metadata={
            "name": "CommercialProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
