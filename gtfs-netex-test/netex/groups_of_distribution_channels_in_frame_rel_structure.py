from dataclasses import dataclass, field
from typing import List
from netex.frame_containment_structure import FrameContainmentStructure
from netex.group_of_distribution_channels import GroupOfDistributionChannels

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupsOfDistributionChannelsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of DISTRIBUTION CHANNEL.
    """
    class Meta:
        name = "groupsOfDistributionChannelsInFrame_RelStructure"

    group_of_distribution_channels: List[GroupOfDistributionChannels] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
