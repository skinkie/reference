from dataclasses import dataclass, field
from typing import List, Optional

from .extensions_1 import Extensions1
from .natural_language_string_structure import NaturalLanguageStringStructure
from .operational_unit_ref_structure import OperationalUnitRefStructure
from .operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedOperatorStructure:
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_short_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operational_unit_ref: List[OperationalUnitRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
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
