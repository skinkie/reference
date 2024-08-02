from dataclasses import dataclass, field
from typing import Optional

from .natural_language_string_structure import NaturalLanguageStringStructure
from .values_structure import ValuesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ValueSetStructure:
    value_set_code: str = field(
        metadata={
            "name": "ValueSetCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    class_of_values: str = field(
        metadata={
            "name": "ClassOfValues",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    values: ValuesStructure = field(
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
