from dataclasses import dataclass, field
from typing import List
from netex.group_of_services_member_structure import GroupOfServicesMemberStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfServicesMembersRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of Member of GROUP OF SERVICE Member.

    :ivar group_of_services_member: Member of GROUP OF SERVICE Garage
        Member.
    """
    class Meta:
        name = "groupOfServicesMembers_RelStructure"

    group_of_services_member: List[GroupOfServicesMemberStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfServicesMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
