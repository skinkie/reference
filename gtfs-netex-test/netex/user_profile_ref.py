from dataclasses import dataclass
from netex.user_profile_ref_structure import UserProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfileRef(UserProfileRefStructure):
    """
    Reference to a USER PROFILE usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
