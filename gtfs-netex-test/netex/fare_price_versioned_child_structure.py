from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.capping_rule_price_ref import CappingRulePriceRef
from netex.controllable_element_price_ref import ControllableElementPriceRef
from netex.customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from netex.discounting_rule import DiscountingRule
from netex.discounting_rule_ref import DiscountingRuleRef
from netex.distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from netex.fare_price_ref import FarePriceRef
from netex.fare_product_price_ref import FareProductPriceRef
from netex.fare_structure_element_price_ref import FareStructureElementPriceRef
from netex.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from netex.geographical_interval_price_ref import GeographicalIntervalPriceRef
from netex.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.limiting_rule import LimitingRule
from netex.limiting_rule_in_context import LimitingRuleInContext
from netex.limiting_rule_ref import LimitingRuleRef
from netex.multilingual_string import MultilingualString
from netex.parking_price_ref import ParkingPriceRef
from netex.price_rule_step_results_rel_structure import PriceRuleStepResultsRelStructure
from netex.price_unit_ref import PriceUnitRef
from netex.pricing_rule import PricingRule
from netex.pricing_rule_ref import PricingRuleRef
from netex.pricing_service_ref import PricingServiceRef
from netex.private_code import PrivateCode
from netex.quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from netex.rounding_ref import RoundingRef
from netex.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from netex.series_constraint_price_ref import SeriesConstraintPriceRef
from netex.time_interval_price_ref import TimeIntervalPriceRef
from netex.time_unit_price_ref import TimeUnitPriceRef
from netex.usage_parameter_price_ref import UsageParameterPriceRef
from netex.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePriceVersionedChildStructure(VersionedChildStructure):
    """
    Type for FARE PRICE.

    :ivar name: Name of FARE PRICE.
    :ivar description: Description of FARE PRICE.
    :ivar private_code:
    :ivar start_date: Start date for selling product or service at the
        PRICE.
    :ivar end_date: End date for selling product or services at the
        PRICE.
    :ivar amount: PRICE amount. in specified currency.
    :ivar currency: Currency of Price ISO 4217.
    :ivar price_unit_ref:
    :ivar units: Other units for PRICE (If not in a currency).
    :ivar rule_step_results: Interim amounts for any pricing rules
        applied to derive price , for example VAT amount  charged.
        +v1.1
    :ivar is_allowed: Whether the PRICE is allowed.
    :ivar pricing_service_ref:
    :ivar choice:
    :ivar choice_1:
    :ivar can_be_cumulative: Whether this discount can be used
        cumulatively with other discounts.
    :ivar rounding_ref:
    :ivar ranking: Ranking to give this discount relatove to other
        applicable discounts.
    """
    class Meta:
        name = "FarePrice_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
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
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
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
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
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
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice_1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRuleInContext",
                    "type": LimitingRuleInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitingRule",
                    "type": LimitingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRule",
                    "type": DiscountingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRule",
                    "type": PricingRule,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    can_be_cumulative: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanBeCumulative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ranking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
