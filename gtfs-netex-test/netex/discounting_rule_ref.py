from dataclasses import dataclass

from .discounting_rule_ref_structure import DiscountingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DiscountingRuleRef(DiscountingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
