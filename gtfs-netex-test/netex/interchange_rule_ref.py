from dataclasses import dataclass
from netex.interchange_rule_ref_structure import InterchangeRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleRef(InterchangeRuleRefStructure):
    """
    Reference to an INTERCHANGE RULE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
