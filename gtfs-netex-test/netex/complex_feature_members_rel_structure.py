from dataclasses import dataclass, field
from typing import List
from .complex_feature_member_versioned_child_structure import (
    ComplexFeatureMemberVersionedChildStructure,
)
from .containment_aggregation_structure import ContainmentAggregationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ComplexFeatureMembersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "complexFeatureMembers_RelStructure"

    complex_feature_member: List[
        ComplexFeatureMemberVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "ComplexFeatureMember",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
