from dataclasses import dataclass
from .interchange_rule_version_structure import InterchangeRuleVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRule(InterchangeRuleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
