from dataclasses import dataclass, field

from .uic_product_characteristic_enumeration import UicProductCharacteristicEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UicProductCharacteristicList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[UicProductCharacteristicEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
