from dataclasses import dataclass, field
from typing import List, Optional

from .advice_ref_structure import AdviceRefStructure
from .advice_type_enumeration import AdviceTypeEnumeration
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PtAdviceStructure:
    advice_ref: Optional[AdviceRefStructure] = field(
        default=None,
        metadata={
            "name": "AdviceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice_type: Optional[AdviceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AdviceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdviceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    details: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
