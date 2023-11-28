from dataclasses import dataclass
from netex.discounting_rule_ref_structure import DiscountingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DiscountingRuleRef(DiscountingRuleRefStructure):
    """
    Reference to a DISCOUNTING RULE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
