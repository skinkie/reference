from dataclasses import dataclass, field
from typing import List, Optional

from .extensions_1 import Extensions1
from .half_open_timestamp_input_range_structure import HalfOpenTimestampInputRangeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .remedy_type_enumeration import RemedyTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RemedyStructure:
    remedy_type: Optional[RemedyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RemedyType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    remedy_period: Optional[HalfOpenTimestampInputRangeStructure] = field(
        default=None,
        metadata={
            "name": "RemedyPeriod",
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
