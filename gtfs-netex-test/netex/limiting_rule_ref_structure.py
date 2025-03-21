from dataclasses import dataclass

from .discounting_rule_ref_structure import DiscountingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LimitingRuleRefStructure(DiscountingRuleRefStructure):
    pass
