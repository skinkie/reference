from dataclasses import dataclass, field
from typing import List
from netex.uic_product_characteristic_enumeration import UicProductCharacteristicEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicProductCharacteristicList:
    """
    List of UIC Product Characteristics UIC 7139 Code list.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[UicProductCharacteristicEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
