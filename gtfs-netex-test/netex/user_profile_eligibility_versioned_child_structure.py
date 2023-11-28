from dataclasses import dataclass, field
from typing import Optional
from netex.companion_profile_ref import CompanionProfileRef
from netex.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure
from netex.user_profile_ref import UserProfileRef
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfileEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    """
    Type for USER PROFILE ELIGIBILITY.
    """
    class Meta:
        name = "UserProfileEligibility_VersionedChildStructure"

    vehicle_pooler_profile_ref_or_companion_profile_ref_or_user_profile_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolerProfileRef",
                    "type": VehiclePoolerProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
