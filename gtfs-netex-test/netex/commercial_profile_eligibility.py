from dataclasses import dataclass, field
from netex.commercial_profile_eligibility_versioned_child_structure import CommercialProfileEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileEligibility(CommercialProfileEligibilityVersionedChildStructure):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific COMMERCIAL PROFILE as a validity parameter.

    :ivar id: Identifier of COMMERCIAL PROFILE ELIGIBILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
