from dataclasses import dataclass
from netex.interchange_rule_parameter_structure import InterchangeRuleParameterStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleFilter(InterchangeRuleParameterStructure):
    """
    Filter for  INTERCHANGE RULE Filter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
