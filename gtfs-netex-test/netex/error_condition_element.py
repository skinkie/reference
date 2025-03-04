from dataclasses import dataclass

from .error_condition_element_structure import ErrorConditionElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class ErrorConditionElement(ErrorConditionElementStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
