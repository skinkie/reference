from dataclasses import dataclass, field
from netex.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Reselling(ResellingVersionStructure):
    """
    Common resale conditions (i.e. for exchange or refund) attaching to the
    product.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
