from dataclasses import dataclass
from netex.type_of_pricing_rule_ref_structure import TypeOfPricingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPricingRuleRef(TypeOfPricingRuleRefStructure):
    """Reference to a TYPE OF PRICING RULE.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
