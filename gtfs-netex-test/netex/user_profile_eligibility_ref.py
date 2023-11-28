from dataclasses import dataclass
from netex.user_profile_eligibility_ref_structure import UserProfileEligibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfileEligibilityRef(UserProfileEligibilityRefStructure):
    """
    Reference to a USER PROFILE ELIGIBILITY..
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
