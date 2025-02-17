from dataclasses import dataclass, field

from .uic_product_characteristic_enumeration import UicProductCharacteristicEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class UicProductCharacteristic:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: UicProductCharacteristicEnumeration = field(
        metadata={
            "required": True,
        }
    )
