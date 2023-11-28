from dataclasses import dataclass, field
from netex.user_profile_version_structure import UserProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfile(UserProfileVersionStructure):
    """
    The social profile of a passenger, based on age group, education, profession,
    social status, sex etc., often used for allowing discounts: 18-40 years old,
    graduates, drivers, unemployed, women etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
