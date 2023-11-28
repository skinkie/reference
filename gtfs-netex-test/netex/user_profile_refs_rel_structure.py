from dataclasses import dataclass, field
from typing import List
from netex.companion_profile_ref import CompanionProfileRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.user_profile_ref import UserProfileRef
from netex.vehicle_pooler_profile_ref import VehiclePoolerProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UserProfileRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of USAGE PROFILEs.
    """
    class Meta:
        name = "userProfileRefs_RelStructure"

    vehicle_pooler_profile_ref_or_companion_profile_ref_or_user_profile_ref: List[object] = field(
        default_factory=list,
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
