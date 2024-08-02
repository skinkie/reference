from dataclasses import dataclass, field
from typing import List, Union

from .type_of_value import TypeOfValue
from .value_set import ValueSet

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TypesOfValueStructure:
    value_set_or_type_of_value: List[Union[ValueSet, TypeOfValue]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValueSet",
                    "type": ValueSet,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "TypeOfValue",
                    "type": TypeOfValue,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
