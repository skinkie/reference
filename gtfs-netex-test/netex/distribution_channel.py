from dataclasses import dataclass, field
from netex.distribution_channel_version_structure import DistributionChannelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistributionChannel(DistributionChannelVersionStructure):
    """
    A type of outlet for selling a product.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
