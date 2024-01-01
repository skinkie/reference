from dataclasses import dataclass
from .interchange_rule_ref_structure import InterchangeRuleRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleRef(InterchangeRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
