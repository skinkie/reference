from dataclasses import dataclass

from .capping_rule_ref_structure import CappingRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CappingRuleRef(CappingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
