from dataclasses import dataclass, field
from netex.refunding_version_structure import RefundingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Refunding(RefundingVersionStructure):
    """
    Whether and how the product may be refunded.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
