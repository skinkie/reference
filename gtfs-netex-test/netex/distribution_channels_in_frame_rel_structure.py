from dataclasses import dataclass, field
from typing import List
from netex.distribution_channel import DistributionChannel
from netex.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionChannelsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of DISTRIBUTION CHANNEL.
    """
    class Meta:
        name = "distributionChannelsInFrame_RelStructure"

    distribution_channel: List[DistributionChannel] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
