from dataclasses import dataclass, field
from typing import List
from netex.amount_of_price_unit_product import AmountOfPriceUnitProduct
from netex.capped_discount_right import CappedDiscountRight
from netex.frame_containment_structure import FrameContainmentStructure
from netex.preassigned_fare_product import PreassignedFareProduct
from netex.sale_discount_right import SaleDiscountRight
from netex.supplement_product import SupplementProduct
from netex.third_party_product import ThirdPartyProduct
from netex.usage_discount_right import UsageDiscountRight

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FARE PRODUCT.
    """
    class Meta:
        name = "fareProductsInFrame_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
