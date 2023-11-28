from dataclasses import dataclass, field
from netex.subscribing_version_structure import SubscribingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Subscribing(SubscribingVersionStructure):
    """Parameters relating to paying by Subscribing for a product.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
