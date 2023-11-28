from dataclasses import dataclass, field
from typing import Optional
from netex.user_profile_ref_structure import UserProfileRefStructure
from netex.user_profile_version_structure import UserProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolerProfileVersionStructure(UserProfileVersionStructure):
    """
    Type for VEHICLE POOLER PROFILE.

    :ivar host_user_profile_ref: Host uder profile offering these pooler
        prferences
    :ivar smoking_allowed: Whether pets are  is allowed by the host
        pooler.
    :ivar pets_allowed: Whether smoking  is allowed by the host pooler.
    :ivar luggage_allowed: Whether the pooler is prepared to carry
        luggage for the passenger. The nature of the luggage accepted
        can be specified by one or more separate LUGGAGE ALLOWANCE
        elements. (It may be different on different journeys)
    :ivar detour_accepted: Whether the pooler is prepared to make a
        detour.
    """
    class Meta:
        name = "VehiclePoolerProfile_VersionStructure"

    host_user_profile_ref: Optional[UserProfileRefStructure] = field(
        default=None,
        metadata={
            "name": "HostUserProfileRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    smoking_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmokingAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pets_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PetsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    luggage_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LuggageAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    detour_accepted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DetourAccepted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
