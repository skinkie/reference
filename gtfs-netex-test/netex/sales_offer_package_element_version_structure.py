from dataclasses import dataclass, field
from typing import Optional
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.condition_summary import ConditionSummary
from netex.fare_product_ref import FareProductRef
from netex.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.sales_offer_package_prices_rel_structure import SalesOfferPackagePricesRelStructure
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.supplement_product_ref import SupplementProductRef
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef
from netex.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesOfferPackageElementVersionStructure(PriceableObjectVersionStructure):
    """
    Type for SALES OFFER PACKAGE ELEMENT.

    :ivar requires_validation: Whether element requires validation
        before it can be used.
    :ivar condition_summary:
    :ivar sales_offer_package_ref:
    :ivar type_of_travel_document_ref:
    :ivar choice:
    :ivar validity_parameter_assignments: VALIDITY PARAMETER ASSIGNMENTs
        associated with SALES OFFER PACKAGE ELEMENT.
    :ivar prices: PRICEs of SALES OFFER PACKAGE ELEMENT.
    :ivar order: Relative order of element.
    """
    class Meta:
        name = "SalesOfferPackageElement_VersionStructure"

    requires_validation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresValidation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    condition_summary: Optional[ConditionSummary] = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: Optional[object] = field(
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
    validity_parameter_assignments: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[SalesOfferPackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
