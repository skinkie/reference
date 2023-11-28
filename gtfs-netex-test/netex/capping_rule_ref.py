from dataclasses import dataclass
from netex.capping_rule_ref_structure import CappingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CappingRuleRef(CappingRuleRefStructure):
    """
    Reference to a CAPPING RULE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
