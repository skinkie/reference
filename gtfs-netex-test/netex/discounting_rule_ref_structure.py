from dataclasses import dataclass
from netex.pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DiscountingRuleRefStructure(PricingRuleRefStructure):
    """
    Type for Reference to a DISCOUNTING RULE.
    """
