from dataclasses import dataclass, field
from netex.user_profile_eligibility_versioned_child_structure import UserProfileEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfileEligibility(UserProfileEligibilityVersionedChildStructure):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific USER PROFILE as a validity parameter.

    :ivar id: Identifier of USER PROFILE ELIGIBILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
