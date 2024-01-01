from dataclasses import dataclass
from .interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleFilter(InterchangeRuleParameterStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
