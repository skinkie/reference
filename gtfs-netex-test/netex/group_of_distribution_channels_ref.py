from dataclasses import dataclass

from .group_of_distribution_channels_ref_structure import GroupOfDistributionChannelsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfDistributionChannelsRef(GroupOfDistributionChannelsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
