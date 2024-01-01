from dataclasses import dataclass
from .error_condition_structure import ErrorConditionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCondition(ErrorConditionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
