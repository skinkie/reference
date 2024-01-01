from dataclasses import dataclass
from .limiting_rule_ref_structure import LimitingRuleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRuleRef(LimitingRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
