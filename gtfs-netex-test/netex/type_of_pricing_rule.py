from dataclasses import dataclass

from .type_of_pricing_rule_version_structure import TypeOfPricingRuleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfPricingRule(TypeOfPricingRuleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
