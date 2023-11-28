from dataclasses import dataclass
from netex.limiting_rule_ref_structure import LimitingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LimitingRuleRef(LimitingRuleRefStructure):
    """
    Reference to a LIMITING RULE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
