from dataclasses import dataclass
from .validity_condition_ref_structure import ValidityConditionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityConditionRef(ValidityConditionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
