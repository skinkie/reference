from dataclasses import dataclass
from netex.pricing_rule_ref_structure import PricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingRuleRef(PricingRuleRefStructure):
    """
    Reference to a PRICING RULE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
