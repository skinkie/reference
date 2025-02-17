from dataclasses import dataclass

from .pricing_rule_versioned_structure import PricingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PricingRule(PricingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
