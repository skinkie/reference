from dataclasses import dataclass, field
from netex.uic_product_characteristic_enumeration import UicProductCharacteristicEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicProductCharacteristic:
    """Classification of UIC Product Characteristics type - UIC 7139 Code list."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: UicProductCharacteristicEnumeration = field(
        metadata={
            "required": True,
        }
    )
