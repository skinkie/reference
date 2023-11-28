from dataclasses import dataclass
from netex.all_distribution_channels_ref_structure_element import AllDistributionChannelsRefStructureElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllDistributionChannelsRef(AllDistributionChannelsRefStructureElement):
    """
    Reference to   All DISTRIBUTION CHANNELs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
