from dataclasses import dataclass, field
from typing import Optional
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.fare_product_ref import FareProductRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.supplement_product_ref import SupplementProductRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a FARE PRODUCT PRICE.
    """
    class Meta:
        name = "FareProductPrice_VersionedChildStructure"

    choice_2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
