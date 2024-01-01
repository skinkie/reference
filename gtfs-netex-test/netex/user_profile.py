from dataclasses import dataclass
from .user_profile_version_structure import UserProfileVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UserProfile(UserProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
