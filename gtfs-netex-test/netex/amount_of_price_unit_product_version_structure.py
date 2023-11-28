from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.amount_of_price_unit_enumeration import AmountOfPriceUnitEnumeration
from netex.fare_product_version_structure import FareProductVersionStructure
from netex.price_unit_ref import PriceUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AmountOfPriceUnitProductVersionStructure(FareProductVersionStructure):
    """
    Type for AMOUNT OF PRICE UNIT PRODUCT.

    :ivar product_type: Classification of PEEASSIGNED FARE PRODUCT.
        +v1.1
    :ivar price_unit_ref:
    :ivar amount: Number of units. If only ine. Otherwise use TARIFF
        with  FARE QUALITY FACTOR to specify a range
    """
    class Meta:
        name = "AmountOfPriceUnitProduct_VersionStructure"

    product_type: Optional[AmountOfPriceUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
