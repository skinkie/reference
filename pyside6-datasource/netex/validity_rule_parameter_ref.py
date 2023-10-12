from dataclasses import dataclass
from netex.validity_rule_parameter_ref_structure import ValidityRuleParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityRuleParameterRef(ValidityRuleParameterRefStructure):
    """Reference to a VALIDITY RULE PARAMETER.

    A user defined VALIDITY CONDITION used by a rule for selecting
    versions.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
