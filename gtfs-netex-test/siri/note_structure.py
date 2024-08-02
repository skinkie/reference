from dataclasses import dataclass, field
from typing import Optional

from .natural_language_string_structure import NaturalLanguageStringStructure
from .situation_full_ref import SituationFullRef
from .situation_ref import SituationRef
from .situation_simple_ref import SituationSimpleRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NoteStructure:
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_simple_ref: Optional[SituationSimpleRef] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_full_ref: Optional[SituationFullRef] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    note: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
