from dataclasses import dataclass
from netex.user_profile_ref_structure import UserProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompanionProfileRefStructure(UserProfileRefStructure):
    """
    Type for Reference to a COMPANION PROFILE usage parameter.
    """
