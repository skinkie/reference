from dataclasses import dataclass
from .user_profile_eligibility_ref_structure import (
    UserProfileEligibilityRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfileEligibilityRef(UserProfileEligibilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
