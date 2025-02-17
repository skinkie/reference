from dataclasses import dataclass

from .interchange_rule_version_structure import InterchangeRuleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class InterchangeRule(InterchangeRuleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
