from dataclasses import dataclass

from .validity_condition_ref_structure import ValidityConditionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ValidityRuleParameterRefStructure(ValidityConditionRefStructure):
    pass
