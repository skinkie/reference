from dataclasses import dataclass
from netex.validity_condition_ref_structure import ValidityConditionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ValidityRuleParameterRefStructure(ValidityConditionRefStructure):
    """
    Type for a reference to a VALIDITY RULE PARAMETER.
    """
