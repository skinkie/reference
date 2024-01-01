from dataclasses import dataclass, field
from typing import List
from .uic_product_characteristic_enumeration import (
    UicProductCharacteristicEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UicProductCharacteristicList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[UicProductCharacteristicEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
