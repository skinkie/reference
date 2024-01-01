from dataclasses import dataclass
from .pricing_rule_versioned_structure import PricingRuleVersionedStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PricingRule(PricingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
