from dataclasses import dataclass, field
from typing import List
from netex.discounting_rule import DiscountingRule
from netex.frame_containment_structure import FrameContainmentStructure
from netex.limiting_rule import LimitingRule
from netex.limiting_rule_in_context import LimitingRuleInContext
from netex.pricing_rule import PricingRule

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingRulesRelStructure(FrameContainmentStructure):
    """
    Ser of PRICING RULEs such for Frame.
    """
    class Meta:
        name = "pricingRules_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
