from dataclasses import dataclass, field
from typing import Union

from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .entitlement_product_ref import EntitlementProductRef
from .fare_product_ref import FareProductRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .service_access_right_ref import ServiceAccessRightRef
from .supplement_product_ref import SupplementProductRef
from .third_party_product_ref import ThirdPartyProductRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceAccessRightRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "serviceAccessRightRefs_RelStructure"

    service_access_right_ref_or_preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref: list[
        Union[EntitlementProductRef, SupplementProductRef, PreassignedFareProductRef, AmountOfPriceUnitProductRef, UsageDiscountRightRef, ThirdPartyProductRef, CappedDiscountRightRef, SaleDiscountRightRef, FareProductRef, ServiceAccessRightRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
