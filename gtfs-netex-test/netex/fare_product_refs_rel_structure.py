from dataclasses import dataclass, field
from typing import List
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.fare_product_ref import FareProductRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.supplement_product_ref import SupplementProductRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareProductRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for references to a FARE PRODUCT.
    """
    class Meta:
        name = "fareProductRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
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
