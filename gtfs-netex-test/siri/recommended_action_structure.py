from dataclasses import dataclass, field
from typing import List, Optional

from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RecommendedActionStructure:
    type_of_action_ref: TypeOfValueRefStructure = field(
        metadata={
            "name": "TypeOfActionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
