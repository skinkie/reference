from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.discounting_rule_ref import DiscountingRuleRef
from netex.limiting_rule_ref import LimitingRuleRef
from netex.multilingual_string import MultilingualString
from netex.price_unit_ref import PriceUnitRef
from netex.pricing_rule_ref import PricingRuleRef
from netex.type_of_pricing_rule_ref import TypeOfPricingRuleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingRuleVersionedStructure(DataManagedObjectStructure):
    """
    Type for PRICING RULE.

    :ivar name: Name of PRICING RULE parameter set.
    :ivar description: Name of PRICING RULE parameter set.
    :ivar method_name: PricingRule method to use.
    :ivar type_of_pricing_rule_ref:
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar factor: Pricing factor to use.
    :ivar currency: Currency unit for amount +v1.1
    :ivar price_unit_ref:
    :ivar url: URLor rule. with infor fmethod to use.
    """
    class Meta:
        name = "PricingRule_VersionedStructure"

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
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_pricing_rule_ref: Optional[TypeOfPricingRuleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: Optional[object] = field(
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
            ),
        }
    )
    factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Factor",
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
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
