from dataclasses import dataclass
from .error_condition_element_structure import ErrorConditionElementStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorConditionElement(ErrorConditionElementStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
