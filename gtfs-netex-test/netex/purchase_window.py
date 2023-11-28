from dataclasses import dataclass, field
from netex.purchase_window_version_structure import PurchaseWindowVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurchaseWindow(PurchaseWindowVersionStructure):
    """
    The number and characteristics of persons entitled to use the public transport
    service instead of the original customer.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
