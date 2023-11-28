from dataclasses import dataclass
from netex.group_of_distribution_channels_ref_structure import GroupOfDistributionChannelsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfDistributionChannelsRef(GroupOfDistributionChannelsRefStructure):
    """
    Reference to a GROUP OF DISTRIBUTION CHANNELs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
