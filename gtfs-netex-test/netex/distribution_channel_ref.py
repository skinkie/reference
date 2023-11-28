from dataclasses import dataclass
from netex.distribution_channel_ref_structure_element import DistributionChannelRefStructureElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionChannelRef(DistributionChannelRefStructureElement):
    """
    Reference to a DISTRIBUTION CHANNEL.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
