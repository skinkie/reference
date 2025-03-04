from dataclasses import dataclass, field

from .distribution_channel_ref import DistributionChannelRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DistributionChannelRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "distributionChannelRefs_RelStructure"

    distribution_channel_ref: list[DistributionChannelRef] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
