from dataclasses import dataclass, field
from typing import Optional
from .fare_product_version_structure import FareProductVersionStructure
from .preassigned_fare_product_enumeration import (
    PreassignedFareProductEnumeration,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreassignedFareProductVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "PreassignedFareProduct_VersionStructure"

    product_type: Optional[PreassignedFareProductEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
