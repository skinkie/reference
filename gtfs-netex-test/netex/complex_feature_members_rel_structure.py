from dataclasses import dataclass, field
from typing import List
from netex.complex_feature_member_versioned_child_structure import ComplexFeatureMemberVersionedChildStructure
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeatureMembersRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more VALIDITY TRIGGERs.

    :ivar complex_feature_member: Member of a COMPLEX FEATURE.
    """
    class Meta:
        name = "complexFeatureMembers_RelStructure"

    complex_feature_member: List[ComplexFeatureMemberVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
